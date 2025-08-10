"""Service layer."""

from dependency_injector import containers, providers

from app.internal.repository import Repositories, postgresql
from app.pkg.clients import Clients

from app.internal.services.website_scraper import WebsiteScraperService
from app.internal.services.fsm import FSMService
from app.internal.services.openai import OpenAIService
from app.internal.services.supported_programms import SupportedProgrammsService
from app.internal.services.user_specifics import UserSpecificsService
from app.pkg.settings import settings
from app.pkg.settings.settings import Settings


class Services(containers.DeclarativeContainer):
    """Containers with services."""

    configuration: Settings = providers.Configuration(
        name="settings",
        pydantic_settings=[settings],
    )

    repositories: postgresql.Repositories = providers.Container(Repositories.postgres)

    clients: Clients = providers.Container(Clients)

    # Services

    website_scraper_service = providers.Singleton(
        WebsiteScraperService,
        minio_client=clients.minio_client,
        supported_programms_repository=repositories.supported_programms_repository,
    )

    supported_programms_service = providers.Singleton(
        SupportedProgrammsService,
        supported_programms_repository=repositories.supported_programms_repository,
    )

    user_specifics_service = providers.Singleton(
        UserSpecificsService,
        user_specifics_repository=repositories.user_specifics_repository,
    )

    openai_service = providers.Singleton(
        OpenAIService,
        openai_client=clients.openai_client,
        model=settings.OPENAI.MODEL_NAME,
    )

    fsm_service = providers.Singleton(
        FSMService,
        supported_programms_service=supported_programms_service,
        user_specifics_service=user_specifics_service,
        openai_service=openai_service,
        redis_client=clients.redis_client,
        telegram_client=clients.telegram_client,
    )
