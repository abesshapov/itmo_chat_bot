"""Factory exception for client layer."""

import typing

from app.pkg.models.base.exception import BaseWorkerException


class ClientExceptionFactory(BaseWorkerException):
    """Factory for client exceptions."""

    def __init__(
        self,
        message: str,
        details: typing.Optional[typing.Union[str, Exception]] = None,
    ):
        super().__init__(details=details, message=message)
