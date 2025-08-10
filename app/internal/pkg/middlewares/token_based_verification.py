"""Secret token based authentication."""

from fastapi import Request

from app.pkg.models.exceptions.token_verification import InvalidSecretToken
from app.pkg.settings import settings

__all__ = ["token_based_verification"]


async def token_based_verification(
    request: Request,
):
    """This function is used for routers that need to be protected by secret
    token- based authentication.

    Notes:
        Token for access to WEBHOOKS is X-Telegram-Bot-Api-Secret-Token from header
        and gets from :attr:`.Settings.TELEGRAM.SECRET_TOKEN`.

    Args:
        secret_token_header:
            X-Telegram-Bot-Api-Secret-Token from header.

    Examples:
        You can use this function in your specific router like this::

            >>> from fastapi import APIRouter, Depends
            >>>
            >>> from app.internal.pkg.middlewares.token_based_verification import (
            ...     token_based_verification
            ... )
            >>>
            >>> router = APIRouter(dependencies=[Depends(token_based_verification)])
            >>>
            >>> @router.get("/test")
            ... async def test():
            ...     return {"message": "Hello World!"}

        Or you can use token-based authentication in your global point of application in
        :func:`.create_app` function like this::

            >>> from fastapi import FastAPI
            >>> app = FastAPI(dependencies=[Depends(token_based_verification)])

    Raises:
        InvalidCredentials:
            If X-Telegram-Bot-Api-Secret-Token from header not equal to
            SECRET_TOKEN from settings.

    See Also: https://fastapi.tiangolo.com/tutorial/security/first-steps/

    Returns:
        None
    """
    value = settings.TELEGRAM.SECRET_TOKEN.get_secret_value()
    if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != value:
        raise InvalidSecretToken
