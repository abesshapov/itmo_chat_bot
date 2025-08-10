"""Enums for openai client."""

from app.pkg.models.base import BaseEnum


class Methods(BaseEnum):  # pylint: disable=C0115
    GET: str = "GET"
    POST: str = "POST"
