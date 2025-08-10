"""Telegram client response models."""

from typing import Optional

import pydantic
from pydantic.fields import Field

from app.pkg.clients.telegram.models import BaseTelegramClient
from app.pkg.clients.telegram.models.request import (
    ChatFullInfo,
    ChatMember,
    File,
    Message,
)


# pylint: disable=C0103
class TelegramAPIBaseResponse(BaseTelegramClient):
    """Telegram API response model."""

    ok: bool = Field(
        description="Determines, if request went OK.",
        example=True,
    )


class TelegramAPIGetChatResponse(TelegramAPIBaseResponse):
    """Telegram API get chat response."""

    result: ChatFullInfo = Field(
        description="Full information on the chat.",
    )


class TelegramAPIGetChatMemberResponse(TelegramAPIBaseResponse):
    """Telegram API get chat member response."""

    result: ChatMember = Field(
        description="Chat member information.",
    )


class TelegramAPIDeleteMessageResponse(TelegramAPIBaseResponse):
    """Telegram API message deletion response."""

    result: bool = Field(
        description="Determines if deletion was successful.",
        example=True,
    )


class TelegramAPIWebhookResponse(TelegramAPIBaseResponse):
    """Telegram API webhook operations response."""

    result: bool = Field(
        description="Determines if result is present for request.",
        example=True,
    )

    description: str = Field(
        description="Description of the result.",
        example="Webhook is already set",
    )


class TelegramAPISendMessageResponse(TelegramAPIBaseResponse):
    """Telegram API send message response."""

    result: Optional[Message] = Field(
        default=None,
        description="Sent message instance.",
    )

    error_code: Optional[pydantic.PositiveInt] = Field(
        description="Error code.",
    )

    description: Optional[str] = Field(
        description="Description of the result.",
        example="Webhook is already set",
    )


class TelegramFileResponse(TelegramAPIBaseResponse):
    """Telegram API file response."""

    result: Optional[File] = Field(
        default=None,
        description="File ID.",
    )

    error_code: Optional[pydantic.PositiveInt] = Field(
        description="Error code.",
    )

    description: Optional[str] = Field(
        description="Description of the result.",
        example="Webhook is already set",
    )
