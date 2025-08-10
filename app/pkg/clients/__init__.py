"""Clients module."""

from dependency_injector import containers, providers

from app.pkg.clients.minio.client import MinioClient
from app.pkg.clients.openai.client import OpenaiClient
from app.pkg.settings import settings

from app.pkg.settings.settings import Settings

from app.pkg.clients.redis.client import RedisClient
from app.pkg.clients.telegram import TelegramClient


class Clients(containers.DeclarativeContainer):
    """Containers with clients."""

    configuration: Settings = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    telegram_client: TelegramClient = providers.Singleton(
        TelegramClient,
        bot_token=configuration.TELEGRAM.BOT_TOKEN,
        api_base_url="https://api.telegram.org",
        fs_base_url="https://api.telegram.org/file",
    )

    redis_client = providers.Singleton(
        RedisClient,
    )

    minio_client: MinioClient = providers.Singleton(
        MinioClient,
        bucket_name=configuration.S3.BUCKET_NAME,
        access_key_id=configuration.S3.ROOT_USER,
        secret_access_key=configuration.S3.ROOT_PASSWORD,
        host=configuration.S3.HOST,
        port=configuration.S3.PORT,
    )

    openai_client = providers.Singleton(
        OpenaiClient,
        api_key=configuration.OPENAI.API_KEY,
    )
