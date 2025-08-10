"""Supported program model fields."""

from typing import List, Optional
import uuid

from pydantic import Field

from app.pkg.models.base import BaseModel


class BaseSupportedProgram(BaseModel):
    """Base model for supported program."""


class SupportedProgramFields:
    """Supported program fields."""

    class Identifiers(BaseSupportedProgram):
        """Supported program identifiers."""

        id: uuid.UUID = Field(
            description="Supported program identifier.",
        )

    class Name(BaseSupportedProgram):
        """Supported program name."""

        name: str = Field(
            description="Name of the supported program.",
        )

    class WebsiteUrl(BaseSupportedProgram):
        """Supported program website URL."""

        website_url: str = Field(
            description="Website URL of the supported program.",
        )
