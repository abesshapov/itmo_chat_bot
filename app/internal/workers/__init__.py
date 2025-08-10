"""Workers package."""

from dependency_injector import containers, providers

from app.internal.services import Services
from app.pkg.clients import Clients

from app.internal.workers.website_scraper import WebsiteScraperWorker


class Workers(containers.DeclarativeContainer):
    """Workers container."""

    clients: Clients = providers.Container(Clients)

    services: Services = providers.Container(Services)

    website_scraper_worker = providers.Singleton(
        WebsiteScraperWorker,
        website_scraper_service=services.website_scraper_service,
        interval_between_jobs=3600,
    )
