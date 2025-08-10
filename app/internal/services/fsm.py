"""FSM service implementation."""

from logging import Logger
from typing import Callable, Dict, List, Optional


import pydantic
from app.pkg.clients.redis import RedisClient
from app.pkg.clients.telegram import TelegramClient
from app.pkg.clients.telegram.models.request import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    Update,
)
from app.pkg.clients.telegram.models.response import TelegramAPISendMessageResponse
from app.pkg.logger import get_logger
from app.pkg.models.app.fsm import FSMRouter, StateInformation, States, UpdateTypes
from app.internal.services.supported_programms import SupportedProgrammsService
from app.internal.services.openai import OpenAIService
from app.internal.services.user_specifics import UserSpecificsService


class FSMService:
    """FSM service.

    Whenever a client update is received from telegram bot, it is being
    processed according to configured FSM.
    """

    __logger: Logger = get_logger(__name__)
    __supported_programs_service: SupportedProgrammsService
    __user_specifics_service: UserSpecificsService
    __openai_service: OpenAIService
    __redis_client: RedisClient
    __telegram_client: TelegramClient
    __text_routing: Dict[str, FSMRouter]
    __state_routing: Dict[str, FSMRouter]

    def __init__(
        self,
        supported_programms_service: SupportedProgrammsService,
        user_specifics_service: UserSpecificsService,
        openai_service: OpenAIService,
        redis_client: RedisClient,
        telegram_client: TelegramClient,
    ):

        self.__redis_client = redis_client
        self.__telegram_client = telegram_client
        self.__supported_programs_service = supported_programms_service
        self.__openai_service = openai_service
        self.__user_specifics_service = user_specifics_service

        self.__text_routing = {
            "/start": FSMRouter(
                handler=self.__process_start_command,
                validator=lambda _: True,
            ),
            "❓ Задать вопрос о программе": FSMRouter(
                handler=self.__process_question_about_program,
                validator=lambda _: True,
            ),
            "❗️ Получить рекоммендацию": FSMRouter(
                handler=self.__process_get_recommendation,
                validator=lambda _: True,
            ),
            "Вернуться в главное меню": FSMRouter(
                handler=self.__process_return_to_main_menu,
                validator=lambda _: True,
            ),
        }

        self.__state_routing = {
            States.QUESTIONS.value: FSMRouter(
                handler=self.__process_question,
                validator=lambda _: True,
            ),
            States.RECOMMENDATION.value: FSMRouter(
                handler=self.__process_recommendation,
                validator=lambda _: True,
            ),
        }

    async def get_client_state_information(  # noqa: C901
        self,
        client_id: pydantic.PositiveInt,
    ) -> Optional[StateInformation]:
        """Parse client state information from redis."""

        response: dict[bytes, bytes] = (await self.__redis_client.hgetall(client_id))[0]
        if response == {}:
            return None
        try:
            decoded_response = {k.decode(): v.decode() for k, v in response.items()}
            state_information = StateInformation(**decoded_response)
            keys_to_delete = []
            if keys_to_delete:
                await self.__redis_client.hdel(client_id, keys_to_delete)
            return state_information
        except pydantic.ValidationError as ex:
            self.__logger.error(
                "Unexpected error when parsing redis hashmap: %s",
                ex,
            )
            return None

    def __determine_update_type(
        self,
        update: Update,
    ) -> UpdateTypes:
        """Determines message type based on its content."""

        if update.message and update.message.text:
            return UpdateTypes.TEXT
        raise ValueError("Unexpected update type processing.")

    async def __process_update_based_on_its_type(  # noqa: C901
        self,
        update: Update,
        update_type: UpdateTypes,
    ) -> Callable[[Update], TelegramAPISendMessageResponse]:
        """Process update based on its type.

        Returns function to be called.
        """

        if update_type == UpdateTypes.TEXT:
            return await self.__process_message_update(update)
        raise ValueError("Unexpected update type processing.")

    async def __process_message_update(  # noqa: C901
        self,
        update: Update,
    ) -> Callable[[Update], TelegramAPISendMessageResponse]:
        """Process message update.

        Returns function to be called.
        """

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        state = await self.get_client_state_information(client_id)
        template_message_router = self.__text_routing.get(update.message.text)
        if template_message_router:
            if template_message_router.validator(state):
                return template_message_router.handler
            return self.__process_return_to_main_menu

        template_state_router = self.__state_routing.get(state.state)
        if template_state_router:
            if template_state_router.validator(state):
                return template_state_router.handler
        return self.__process_return_to_main_menu

    async def process_update(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Process bot update."""

        try:
            update_type = self.__determine_update_type(update)
            self.__logger.info(
                "Processing update: %s of type %s.",
                update.json(exclude_none=True),
                update_type,
            )
            function = await self.__process_update_based_on_its_type(
                update,
                update_type,
            )
            result = await function(update)
        except Exception as ex:  # pylint: disable=broad-exception-caught
            try:
                self.__logger.error(
                    "Unexpected error when processing update: %s",
                    ex,
                )
                result = await self.__process_return_to_main_menu(update)
            except Exception as inner_ex:  # pylint: disable=broad-exception-caught
                self.__logger.error(
                    "While handling previous exception, another was raised: %s",
                    inner_ex,
                )
                result = []
        self.__logger.info(
            "Processing result: %s.",
            [
                message.result.json(exclude_none=True)
                for message in result
                if message.result
            ],
        )
        return result

    async def __process_start_command(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of start command."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        await self.__redis_client.delete(client_id)
        await self.__redis_client.hmset(
            client_id,
            StateInformation(
                state=States.MAIN_MENU,
            ).to_dict(exclude_none=True),
        )
        supported_programs = await self.__supported_programs_service.get_programs()
        responses = [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text="""Привет!
Я помогу тебе с выбором программы для поступления в магистратуру ИТМО""",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text=program.name,
                                url=program.website_url,
                            ),
                        ]
                        for program in supported_programs
                    ],
                ),
            ),
        ]
        responses.extend(await self.__process_return_to_main_menu(update))
        return responses

    async def __process_return_to_main_menu(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of return to main menu."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        await self.__redis_client.hmset(
            client_id,
            StateInformation(
                state=States.MAIN_MENU,
            ).to_dict(exclude_none=True),
        )
        return [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text="""С чем я могу помочь?""",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(
                                text="❓ Задать вопрос о программе",
                            ),
                        ],
                        [
                            KeyboardButton(
                                text="❗️ Получить рекоммендацию",
                            ),
                        ],
                    ],
                    resize_keyboard=True,
                    is_persistent=True,
                ),
            ),
        ]

    async def __process_question_about_program(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of question about program."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        await self.__redis_client.hmset(
            client_id,
            StateInformation(
                state=States.QUESTIONS,
            ).to_dict(exclude_none=True),
        )
        return [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text="""Задай свой вопрос о программе, и я постараюсь на него ответить!""",  # pylint: disable=line-too-long
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(
                                text="Вернуться в главное меню",
                            ),
                        ],
                    ],
                    resize_keyboard=True,
                    is_persistent=True,
                ),
            ),
        ]

    async def __process_question(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of question."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )

        question = update.message.text
        self.__logger.info("Received question: %s", question)
        await self.__telegram_client.send_message(
            chat_id=client_id,
            text="Пожалуйста, подожди, я ищу ответ на твой вопрос...",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(
                            text="Вернуться в главное меню",
                        ),
                    ],
                ],
                resize_keyboard=True,
                is_persistent=True,
            ),
        )
        programs = await self.__supported_programs_service.get_programs()
        response = await self.__openai_service.answer_question(
            [program.website_url for program in programs],
            question,
        )
        return [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text=response,
                parse_mode="Markdown",
            ),
        ]

    async def __process_get_recommendation(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of get recommendation."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        await self.__redis_client.hmset(
            client_id,
            StateInformation(
                state=States.RECOMMENDATION,
            ).to_dict(exclude_none=True),
        )
        return [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text="""Расскажи мне про себя и я постараюсь подобрать тебе программу, которая тебе подойдет!""",  # pylint: disable=line-too-long
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                            KeyboardButton(
                                text="Вернуться в главное меню",
                            ),
                        ],
                    ],
                    resize_keyboard=True,
                    is_persistent=True,
                ),
            ),
        ]

    async def __process_recommendation(
        self,
        update: Update,
    ) -> List[TelegramAPISendMessageResponse]:
        """Processing of recommendation."""

        client_id = (
            update.message.from_.id if update.message.from_ else update.message.chat.id
        )
        await self.__user_specifics_service.create_user_specific(
            user_id=client_id,
            specific=update.message.text,
        )
        user_specifics = await self.__user_specifics_service.get_user_specifics(
            client_id,
        )
        programs = await self.__supported_programs_service.get_programs()
        response = await self.__openai_service.provide_recommendation(
            [program.website_url for program in programs],
            [specific.specific for specific in user_specifics],
            [program.name for program in programs],
        )
        await self.__telegram_client.send_message(
            chat_id=client_id,
            text="Пожалуйста, подожди, я ищу подходящую для тебя программу...",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(
                            text="Вернуться в главное меню",
                        ),
                    ],
                ],
                resize_keyboard=True,
                is_persistent=True,
            ),
        )
        return [
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text=response.recommendation,
                parse_mode="Markdown",
            ),
            await self.__telegram_client.send_message(
                chat_id=client_id,
                text=f"Рекомендованная программа: {response.recommended_program}",
                parse_mode="Markdown",
            ),
        ]
