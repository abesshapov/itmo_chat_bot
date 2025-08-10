"""Collect response from a node and return model or raise ClientError."""

from functools import wraps

import pydantic

from app.pkg.clients.openai.models.exceptions import ClientExceptionFactory
from app.pkg.models.base import Model


def collect_response(fn):  # noqa: C901
    """Convert response from a node to an annotated model.

    Args:
        fn:
            Target function that contains a request to a node.

    Examples:
        If you have a function that contains a request to a node,
        decorator :func:`.collect_response` will convert the response from a node to
        an annotated model.

    Warnings:
        The function must return a correct dict object.

    Raises:
        ClientExceptionFactory: when a request of `fn` returns some error in body.
    Returns:
        The model that is specified in type hints of `fn`.
    """

    @wraps(fn)
    async def inner(*args: object, **kwargs: object) -> Model:
        try:
            response = await fn(*args, **kwargs)
        except Exception as exc:
            raise ClientExceptionFactory(
                details=exc,
                message="Openai client exception handled!",
            ) from exc
        else:
            if response.status_code in (403, 409):
                raise ClientExceptionFactory(
                    message=response.text,
                    details="Openai client blocked.",
                )
            elif response.status_code // 100 != 2:
                raise ClientExceptionFactory(
                    message=response.text,
                )

            try:
                model = pydantic.parse_obj_as(
                    fn.__annotations__["return"],
                    response.json(),
                )
            except pydantic.ValidationError as exc:
                raise ClientExceptionFactory(
                    details=exc,
                    message=response.text,
                ) from exc
            else:
                return model

    return inner
