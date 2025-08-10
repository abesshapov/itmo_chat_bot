"""FSM-related models."""

from dataclasses import dataclass
from typing import Callable, List, Optional
import uuid

from pydantic import Field

from app.pkg.clients.telegram.models.request import Update
from app.pkg.clients.telegram.models.response import TelegramAPISendMessageResponse
from app.pkg.models.base import BaseEnum, BaseModel


class States(BaseEnum):
    """Possible client states."""

    MAIN_MENU = "main_menu"

    QUESTIONS = "questions"

    RECOMMENDATION = "recommendation"


class UpdateTypes(BaseEnum):
    """Possible types of messages to be processed."""

    TEXT = "text"


class StateInformation(BaseModel):
    """State information model."""

    state: Optional[States] = Field(
        description="Current state for client.",
        example=States.MAIN_MENU,
    )


StateValidator = Callable[[StateInformation], bool]
UpdateHandler = Callable[[Update], List[TelegramAPISendMessageResponse]]


@dataclass
class FSMRouter:
    """Routing of messages."""

    handler: UpdateHandler
    validator: StateValidator
