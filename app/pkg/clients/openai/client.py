"""Openai client implementation."""

import typing
from logging import Logger
from typing import Dict, List

from pydantic import SecretStr

from app.pkg.logger import get_logger

from openai import AsyncOpenAI

from openai.types.chat import ParsedChatCompletion, completion_create_params

_T = typing.TypeVar("_T")


class OpenaiClient:
    """Openai client implementation.

    Make requests to openai API strictly trhough it. If needed, add new
    handler.
    """

    __logger: Logger = get_logger(__name__)
    __openai_client: AsyncOpenAI

    def __init__(
        self,
        api_key: SecretStr,
    ):

        self.__openai_client = AsyncOpenAI(api_key=api_key.get_secret_value())

    async def create_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        response_model: _T,
    ) -> ParsedChatCompletion:
        """Create completion."""

        return await self.__openai_client.beta.chat.completions.parse(
            messages=messages,
            model=model,
            web_search_options=completion_create_params.WebSearchOptions(
                search_context_size="high",
            ),
            response_format=response_model,
        )
