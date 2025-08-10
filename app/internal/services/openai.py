"""OpenAI service."""

from app.pkg.logger import get_logger
from logging import Logger

from app.pkg.clients.openai import OpenaiClient

from pydantic import BaseModel, Field


class QuestionResponse(
    BaseModel,
):
    """Response model for OpenAI question answering."""

    answer: str = Field(
        description="The answer to the question based on the provided websites.",
    )


class RecommendationResponse(
    BaseModel,
):
    """Response model for OpenAI recommendation."""

    recommendation: str = Field(
        description="The recommendation based on the provided websites and specifics.",
    )

    recommended_program: str = Field(
        description="The recommended program based on the provided websites and specifics.",  # pylint: disable=line-too-long
    )


class OpenAIService:
    """Service for interacting with OpenAI API."""

    __logger: Logger = get_logger(__name__)
    __openai_client: OpenaiClient
    __model: str

    def __init__(self, openai_client: OpenaiClient, model: str):
        self.__openai_client = openai_client
        self.__model = model

    async def answer_question(
        self,
        websites: list[str],
        question: str,
    ):
        """Answer a question based on the content of the provided websites."""
        self.__logger.info("Answering question based on websites.")
        try:
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that answers questions "
                        "based on the content of the provided websites: "
                        f"{', '.join(websites)}."
                        "Only answer based on the content of these websites, "
                        "do not make up information. If the answer is not found, "
                        "say 'Я не знаю'. Use russian language for your response."
                        "Do not use formatting,"
                        "but if you do - use HTML only, no markdown."
                    ),
                },
                {
                    "role": "user",
                    "content": f"I have a question: {question}",
                },
            ]
            response = await self.__openai_client.create_completion(
                model=self.__model,
                messages=messages,
                response_model=QuestionResponse,
            )
            return response.choices[0].message.parsed.answer
        except Exception as e:
            self.__logger.error("Error answering question: %s", e)
            raise

    async def provide_recommendation(
        self,
        websites: list[str],
        specifics: list[str],
        programs: list[str],
    ):
        """Provide a recommendation based on the content of the provided
        websites and user specifics."""
        self.__logger.info("Providing recommendation based on websites and specifics.")
        try:
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that provides recommendations "
                        "based on the content of the provided websites:"
                        f"{', '.join(websites)} "
                        f"and user specifics: {'; '.join(specifics)}. "
                        "Only answer based on the content of these websites "
                        "and specifics, do not make up information."
                        "If the answer is not found, "
                        "say 'Я не знаю'. Use russian language for your response."
                        "Do not use formatting, "
                        "but if you do - use HTML only, no markdown."
                        "Also, provide recommended program "
                        f"from the list of supported programs: {', '.join(programs)}."
                        "Besides recommendation, specify courses that can be taken in "
                        "the recommended program."
                    ),
                },
            ]
            response = await self.__openai_client.create_completion(
                model=self.__model,
                messages=messages,
                response_model=RecommendationResponse,
            )
            return response.choices[0].message.parsed
        except Exception as e:
            self.__logger.error("Error providing recommendation: %s", e)
            raise
