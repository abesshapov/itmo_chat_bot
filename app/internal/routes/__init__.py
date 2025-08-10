"""Global point for collected routers. __routes__ is a :class:`.Routes`
instance that contains all routers in your application.

Examples:
    After declaring all routers, you need to register them in your application::

        >>> from fastapi import FastAPI
        >>> app = FastAPI()
        >>> __routes__.register_routes(app=app)
"""
from app.internal.pkg.middlewares.token_based_verification import (
    token_based_verification,
)
from app.pkg.models.base import BaseEnum
from app.pkg.models.core.routes import Routes
from fastapi import APIRouter, Depends


class Tags(BaseEnum):

    WEBHOOKS = "webhooks"


webhooks_router = APIRouter(
    dependencies=[Depends(token_based_verification)],
    prefix="/webhooks",
    tags=[Tags.WEBHOOKS],
)


__routes__ = Routes(
    routers=(webhooks_router,),
)
