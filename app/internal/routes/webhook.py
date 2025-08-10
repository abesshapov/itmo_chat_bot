"""Webhooks router for telegram bot requests processing."""

from dependency_injector.wiring import Provide, inject
from fastapi import Depends
from pydantic import ValidationError

from app.internal.routes import webhooks_router
from app.internal.services import FSMService, Services
from app.pkg.clients.telegram.models.request import Update
from app.pkg.settings import settings


@webhooks_router.post(
    f"{settings.TELEGRAM.BOT_WEBHOOK_PATH}",
)
@inject
async def handle_client_bot_update(
    update: dict,
    fsm_service: FSMService = Depends(
        Provide[Services.fsm_service],
    ),
):
    try:
        update_model = Update(**update)
    except ValidationError:
        return
    await fsm_service.process_update(update_model)
