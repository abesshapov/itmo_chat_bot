"""Telegram client implementation."""

import json
import typing
from logging import Logger
from typing import Any, List, Optional, Union

from httpcore import Response
import httpx
import pydantic
from pydantic.json import pydantic_encoder

from app.pkg.clients.telegram.handlers.collect_response import collect_response
from app.pkg.clients.telegram.models.enums import Methods
from app.pkg.clients.telegram.models.request import (
    ForceReply,
    InlineKeyboardMarkup,
    InlineQueryResult,
    InlineQueryResultsButton,
    InputFile,
    LinkPreviewOptions,
    MessageEntity,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    ReplyParameters,
)
from app.pkg.clients.telegram.models.response import (
    TelegramAPIDeleteMessageResponse,
    TelegramAPIGetChatMemberResponse,
    TelegramAPIGetChatResponse,
    TelegramAPISendMessageResponse,
    TelegramAPIWebhookResponse,
    TelegramFileResponse,
)
from app.pkg.logger import get_logger

_T = typing.TypeVar("_T")


class TelegramClient:
    """Telegram client implementation.

    Make requests to telegram API strictly trhough it. If needed, add
    new handler.
    """

    __logger: Logger = get_logger(__name__)
    __session: httpx.AsyncClient
    __fs_session: httpx.AsyncClient
    __api_base_url: pydantic.HttpUrl
    __fs_base_url: pydantic.HttpUrl

    def __init__(
        self,
        bot_token: pydantic.SecretStr,
        api_base_url: pydantic.HttpUrl,
        fs_base_url: pydantic.HttpUrl,
    ):

        self.__api_base_url = api_base_url
        self.__fs_base_url = fs_base_url
        self.__session = self.__init_httpx_session(bot_token)
        self.__fs_session = self.__init_fs_httpx_session(bot_token)

    def __init_httpx_session(self, token: pydantic.SecretStr) -> httpx.AsyncClient:
        """Initialize httpx sessions."""

        self.__logger.info(
            "Initializing httpx sessions for [%s].",
            self.__class__.__name__,
        )
        return httpx.AsyncClient(
            base_url=f"{self.__api_base_url}/bot{token.get_secret_value()}",
        )

    def __init_fs_httpx_session(self, token: pydantic.SecretStr) -> httpx.AsyncClient:
        """Initialize httpx sessions for file storage."""

        self.__logger.info(
            "Initializing httpx sessions for [%s].",
            self.__class__.__name__,
        )
        return httpx.AsyncClient(
            base_url=f"{self.__fs_base_url}/bot{token.get_secret_value()}",
        )

    async def close(self):
        """Close httpx client session."""

        self.__logger.info("Closing httpx session for [%s].", self.__class__.__name__)
        await self.__session.aclose()

    async def __make_request(
        self,
        *args,
        method: Methods = Methods.POST,
        path: str = "/",
        payload: typing.Optional[typing.Dict[str, typing.Any]] = None,
        params: typing.Optional[typing.Dict[str, typing.Any]] = None,
        files: typing.Optional[Any] = None,
        fs: bool = False,
        **kwargs,
    ) -> _T:
        """Make request to telegram bot API."""

        session = self.__fs_session if fs else self.__session
        return await session.request(
            method=method.value,
            url=path,
            json=payload,
            params=params,
            files=files,
            *args,
            **kwargs,
        )

    @collect_response
    async def set_webhook(
        self,
        webhook_url: pydantic.AnyUrl,
        secret_token: pydantic.SecretStr,
    ) -> TelegramAPIWebhookResponse:
        """Set webhook url for the telegram bot."""

        return await self.__make_request(
            path="/setWebhook",
            params={
                "url": webhook_url,
                "secret_token": secret_token.get_secret_value(),
            },
        )

    @collect_response
    async def delete_webhook(
        self,
    ) -> TelegramAPIWebhookResponse:
        """Delete webhook url from the telegram bot."""

        return await self.__make_request(
            path="/deleteWebhook",
        )

    @collect_response
    async def delete_message(
        self,
        *,
        chat_id: typing.Union[int, str],
        message_id: int,
    ) -> TelegramAPIDeleteMessageResponse:
        """Delete message."""

        return await self.__make_request(
            path="/deleteMessage",
            params={
                "chat_id": chat_id,
                "message_id": message_id,
            },
        )

    @collect_response
    async def send_message(
        self,
        *,
        chat_id: typing.Union[int, str],
        text: str,
        business_connection_id: typing.Optional[str] = None,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> TelegramAPISendMessageResponse:
        """Send message via telegram bot API."""

        return await self.__make_request(
            path="/sendMessage",
            params={
                "chat_id": chat_id,
                "text": text,
                "business_connection_id": business_connection_id,
                "message_thread_id": message_thread_id,
                "parse_mode": parse_mode,
                "entities": json.dumps(entities, default=pydantic_encoder)
                if entities
                else None,
                "link_preview_options": json.dumps(
                    link_preview_options,
                    default=pydantic_encoder,
                )
                if link_preview_options
                else None,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters.json(
                    exclude_none=True,
                )
                if reply_parameters
                else None,
                "reply_markup": reply_markup.json(exclude_none=True)
                if reply_markup
                else None,
            },
        )

    @collect_response
    async def send_document(
        self,
        *,
        chat_id: Union[int, str],
        document: Union["InputFile", str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[Union["InputFile", str]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List["MessageEntity"]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional["ReplyParameters"] = None,
        reply_markup: Optional[
            Union[
                "InlineKeyboardMarkup",
                "ReplyKeyboardMarkup",
                "ReplyKeyboardRemove",
                "ForceReply",
            ]
        ] = None,
        document_name: str = None,
    ) -> TelegramAPISendMessageResponse:
        """Use this method to send general files. On success, the sent Message
        is returned. Bots can currently send files of any type of up to 50 MB
        in size, this limit may be changed in the future.

        :param chat_id: Unique identifier for the target chat or
            username of the target channel (in the format
            @channelusername)
        :param document: File to send. Pass a file_id as String to send
            a file that exists on the Telegram servers (recommended),
            pass an HTTP URL as a String for Telegram to get a file from
            the Internet, or upload a new one using multipart/form-data.
            More information on Sending Files »
        :param business_connection_id: Unique identifier of the business
            connection on behalf of which the message will be sent
        :param message_thread_id: Unique identifier for the target
            message thread (topic) of the forum; for forum supergroups
            only
        :param thumbnail: Thumbnail of the file sent; can be ignored if
            thumbnail generation for the file is supported server-side.
            The thumbnail should be in JPEG format and less than 200 kB
            in size. A thumbnail's width and height should not exceed
            320. Ignored if the file is not uploaded using
            multipart/form-data. Thumbnails can't be reused and can be
            only uploaded as a new file, so you can pass
            “attach://<file_attach_name>” if the thumbnail was uploaded
            using multipart/form-data under <file_attach_name>. More
            information on Sending Files »
        :param caption: Document caption (may also be used when
            resending documents by file_id), 0-1024 characters after
            entities parsing
        :param parse_mode: Mode for parsing entities in the document
            caption. See formatting options for more details.
        :param caption_entities: A JSON-serialized list of special
            entities that appear in the caption, which can be specified
            instead of parse_mode
        :param disable_content_type_detection: Disables automatic
            server-side content type detection for files uploaded using
            multipart/form-data
        :param disable_notification: Sends the message silently. Users
            will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent
            message from forwarding and saving
        :param message_effect_id: Unique identifier of the message
            effect to be added to the message; for private chats only
        :param reply_parameters: Description of the message to reply to
        :param reply_markup: Additional interface options. A JSON-
            serialized object for an inline keyboard, custom reply
            keyboard, instructions to remove a reply keyboard or to
            force a reply from the user
        """

        return await self.__make_request(
            path="/sendDocument",
            params={
                "chat_id": chat_id,
                "document": document if isinstance(document, str) else None,
                "business_connection_id": business_connection_id,
                "message_thread_id": message_thread_id,
                "thumbnail": thumbnail,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": json.dumps(
                    caption_entities,
                    default=pydantic_encoder,
                )
                if caption_entities
                else None,
                "disable_content_type_detection": disable_content_type_detection,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters.json(
                    exclude_none=True,
                )
                if reply_parameters
                else None,
                "reply_markup": reply_markup.json(exclude_none=True)
                if reply_markup
                else None,
            },
            files={"document": (document_name, document)}
            if not isinstance(document, str)
            else None,
        )

    @collect_response
    async def send_photo(
        self,
        *,
        chat_id: Union[int, str],
        photo: Union[InputFile, str],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[ReplyParameters] = None,
        reply_markup: Optional[
            Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
            ]
        ] = None,
    ) -> TelegramAPISendMessageResponse:
        """Send photo via API."""

        return await self.__make_request(
            path="/sendPhoto",
            params={
                "chat_id": chat_id,
                "photo": photo if isinstance(photo, str) else None,
                "business_connection_id": business_connection_id,
                "message_thread_id": message_thread_id,
                "caption": caption,
                "parse_mode": parse_mode,
                "caption_entities": json.dumps(
                    caption_entities,
                    default=pydantic_encoder,
                )
                if caption_entities
                else None,
                "show_caption_above_media": show_caption_above_media,
                "has_spoiler": has_spoiler,
                "disable_notification": disable_notification,
                "protect_content": protect_content,
                "message_effect_id": message_effect_id,
                "reply_parameters": reply_parameters.json(
                    exclude_none=True,
                )
                if reply_parameters
                else None,
                "reply_markup": reply_markup.json(exclude_none=True)
                if reply_markup
                else None,
            },
            files={"photo": photo} if not isinstance(photo, str) else None,
        )

    @collect_response
    async def answer_inline_query(
        self,
        *,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        button: Optional[InlineQueryResultsButton] = None,
    ) -> TelegramAPIDeleteMessageResponse:
        """Use this method to send answers to an inline query. On success, True
        is returned.No more than 50 results per query are allowed.

        :param inline_query_id: Unique identifier for the answered query
        :param results: A JSON-serialized array of results for the
            inline query
        :param cache_time: The maximum amount of time in seconds that
            the result of the inline query may be cached on the server.
            Defaults to 300.
        :param is_personal: Pass True if results may be cached on the
            server side only for the user that sent the query. By
            default, results may be returned to any user who sends the
            same query.
        :param next_offset: Pass the offset that a client should send in
            the next query with the same text to receive more results.
            Pass an empty string if there are no more results or if you
            don't support pagination. Offset length can't exceed 64
            bytes.
        :param button: A JSON-serialized object describing a button to
            be shown above inline query results
        """

        return await self.__make_request(
            path="/answerInlineQuery",
            params={
                "inline_query_id": inline_query_id,
                "results": json.dumps(results, default=pydantic_encoder),
                "cache_time": cache_time,
                "is_personal": is_personal,
                "next_offset": next_offset,
                "button": button.json(exclude_none=True) if button else None,
            },
        )

    @collect_response
    async def answer_callback_query(
        self,
        *,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> TelegramAPIDeleteMessageResponse:
        """Use this method to send answers to callback queries sent from inline
        keyboards. The answer will be displayed to the user as a notification
        at the top of the chat screen or as an alert. On success, True is
        returned.

        :param callback_query_id: Unique identifier for the query to be answered
        :param text: Text of the notification. If not specified, nothing will be shown
        to the user, 0-200 characters
        :param show_alert: If True, an alert will be shown by the client instead of a
            notification at the top of the chat screen. Defaults to false.
        :param url: URL that will be opened by the user's client. If you have created a
            Game and accepted the conditions via @BotFather, specify the URL that
            opens your game - note that this will only work if the query comes
            from a callback_game button.Otherwise, you may use links like
            t.me/your_bot?start=XXXX that open your bot with a parameter.
        :param cache_time: The maximum amount of time in seconds that the result of the
        callback query may be cached client-side. Telegram apps will support caching
            starting in version 3.14. Defaults to 0.
        """

        return await self.__make_request(
            path="/answerCallbackQuery",
            params={
                "callback_query_id": callback_query_id,
                "text": text,
                "show_alert": show_alert,
                "url": url,
                "cache_time": cache_time,
            },
        )

    @collect_response
    async def get_chat(
        self,
        *,
        chat_id: Union[int, str],
    ) -> TelegramAPIGetChatResponse:
        """Use this method to get up-to-date information about the chat.
        Returns a ChatFullInfo object on success.

        :param chat_id: Unique identifier for the target chat or
            username of the target supergroup or channel (in the format
            @channelusername)
        """

        return await self.__make_request(
            path="/getChat",
            params={"chat_id": chat_id},
        )

    @collect_response
    async def get_chat_member(
        self,
        *,
        chat_id: Union[int, str],
        user_id: int,
    ) -> TelegramAPIGetChatMemberResponse:
        """Use this method to get information about a member of a chat. The
        method is only guaranteed to work for other users if the bot is an
        administrator in the chat. Returns a ChatMember object on success.

        :param chat_id: Unique identifier for the target chat or
            username of the target supergroup or channel (in the format
            @channelusername)
        :param user_id: Unique identifier of the target user
        """

        return await self.__make_request(
            path="/getChatMember",
            params={
                "chat_id": chat_id,
                "user_id": user_id,
            },
        )

    @collect_response
    async def edit_message_reply_markup(
        self,
        *,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[TelegramAPISendMessageResponse, bool]:
        """Use this method to edit only the reply markup of messages. On
        success, if the edited message is not an inline message, the edited
        Message is returned, otherwise True is returned. Note that business
        messages that were not sent by the bot and do not contain an inline
        keyboard can only be edited within 48 hours from the time they were
        sent.

        :param business_connection_id: Unique identifier of the business connection
        on behalf of which the message to be edited was sent
        :param chat_id: Required if inline_message_id is not specified.
        Unique identifier for the target chat or username of the target channel
        (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified.
        Identifier of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
        Identifier of the inline message
        :param reply_markup: A JSON-serialized object for an inline keyboard.
        """

        return await self.__make_request(
            path="/editMessageReplyMarkup",
            params={
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "reply_markup": reply_markup.json(exclude_none=True)
                if reply_markup
                else None,
            },
        )

    @collect_response
    async def edit_message_text(
        self,
        *,
        text: str,
        business_connection_id: Optional[str] = None,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List["MessageEntity"]] = None,
        link_preview_options: Optional["LinkPreviewOptions"] = None,
        reply_markup: Optional["InlineKeyboardMarkup"] = None,
    ) -> Union[TelegramAPISendMessageResponse, bool]:
        """Use this method to edit text and game messages. On success, if the
        edited message is not an inline message, the edited Message is
        returned, otherwise True is returned. Note that business messages that
        were not sent by the bot and do not contain an inline keyboard can only
        be edited within 48 hours from the time they were sent.

        :param text: New text of the message, 1-4096 characters after entities parsing
        :param business_connection_id: Unique identifier of the business connection on
        behalf of which the
            message to be edited was sent
        :param chat_id: Required if inline_message_id is not specified.
            Unique identifier for the target chat or username of the target channel
            (in the format @channelusername)
        :param message_id: Required if inline_message_id is not specified.
            Identifier of the message to edit
        :param inline_message_id: Required if chat_id and message_id are not specified.
            Identifier of the inline message
        :param parse_mode: Mode for parsing entities in the message text.
            See formatting options for more details.
        :param entities: A JSON-serialized list of special entities that appear in
            message text, which can be specified instead of parse_mode
        :param link_preview_options: Link preview generation options for the message
        :param reply_markup: A JSON-serialized object for an inline keyboard.
        """

        return await self.__make_request(
            path="/editMessageText",
            params={
                "text": text,
                "business_connection_id": business_connection_id,
                "chat_id": chat_id,
                "message_id": message_id,
                "inline_message_id": inline_message_id,
                "parse_mode": parse_mode,
                "entities": json.dumps(entities, default=pydantic_encoder)
                if entities
                else None,
                "link_preview_options": json.dumps(
                    link_preview_options,
                    default=pydantic_encoder,
                )
                if link_preview_options
                else None,
                "reply_markup": reply_markup.json(exclude_none=True)
                if reply_markup
                else None,
            },
        )

    @collect_response
    async def get_file(
        self,
        *,
        file_id: str,
    ) -> TelegramFileResponse:
        """Use this method to get basic information about a file and prepare it
        for downloading. For the moment, bots can download files of up to 20MB
        in size. On success, a File object is returned. The file can then be
        downloaded via the link
        https://api.telegram.org/file/bot<token>/<file_path>, where.

        <file_path> is taken from the response. It is guaranteed that the link
        will be valid for at least 1 hour. When the link expires, a new one
        can be requested by calling getFile again.

        :param file_id: File identifier to get information about
        """

        return await self.__make_request(
            path="/getFile",
            params={
                "file_id": file_id,
            },
        )

    async def download_file(
        self,
        *,
        file_path: str,
    ) -> Response:
        """Download file from telegram server.

        :param file_path: File path to download
        """

        return await self.__make_request(method=Methods.GET, path=file_path, fs=True)
