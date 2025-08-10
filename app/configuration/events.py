"""``on_startup`` function will be called when server trying to start."""

from contextlib import asynccontextmanager

from dependency_injector.wiring import inject, Provide
from fastapi import FastAPI

from app.pkg.clients import Clients, TelegramClient
from app.internal.workers import Workers, WebsiteScraperWorker
from app.pkg.settings import settings


@asynccontextmanager
@inject
async def lifespan(
    app: FastAPI,  # pylint: disable=unused-argument # noqa: F841
    telegram_client: TelegramClient = Provide[Clients.telegram_client],
    website_scraper_worker: WebsiteScraperWorker = Provide[
        Workers.website_scraper_worker
    ],
) -> None:  # type: ignore
    """Run code on server startup.

    Warnings:
        **Don't use this function for insert default data in database.
        For this action, we have scripts/migrate.py.**

    Returns:
        None
    """

    await telegram_client.set_webhook(
        webhook_url=settings.TELEGRAM.BOT_WEBHOOK_URL,
        secret_token=settings.TELEGRAM.SECRET_TOKEN,
    )
    await website_scraper_worker.run()
    yield
    await telegram_client.delete_webhook()
    await telegram_client.close()
