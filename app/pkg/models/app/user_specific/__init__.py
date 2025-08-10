"""User specific model fields."""

from typing import List, Optional
import uuid

from pydantic import Field, PositiveInt

from app.pkg.models.base import BaseModel


class BaseUserSpecific(BaseModel):
    """Base model for user specific."""


class UserSpecificFields:
    """User specific fields."""

    class UserId(BaseUserSpecific):
        """User specific user identifier."""

        user_id: PositiveInt = Field(
            description="User identifier.",
        )

    class Specific(BaseUserSpecific):
        """User specific data."""

        specific: str = Field(
            description="User specific data.",
        )
