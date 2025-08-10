"""Exceptions for token-based auth verification."""

from starlette import status

from app.pkg.models.base import BaseAPIException

__all__ = ["InvalidSecretToken"]


class InvalidSecretToken(BaseAPIException):
    message = "Invalid credentials."
    status_code = status.HTTP_403_FORBIDDEN
