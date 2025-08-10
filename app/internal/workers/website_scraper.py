"""Website scraper worker."""

import asyncio
from pydantic import PositiveInt
from app.internal.workers.worker import BaseWorker
from app.pkg.logger import get_logger
from app.internal.services.website_scraper import WebsiteScraperService


class WebsiteScraperWorker(
    BaseWorker,
):
    """Report sender worker."""

    __logger = get_logger(__name__)
    __website_scraper_service: WebsiteScraperService
    __interval_between_jobs: PositiveInt

    def __init__(
        self,
        website_scraper_service: WebsiteScraperService,
        interval_between_jobs: PositiveInt,
    ):

        self.__website_scraper_service = website_scraper_service
        self.__interval_between_jobs = interval_between_jobs

    async def run(self):
        """Run worker."""

        while True:
            await self.__website_scraper_service.scrap_websites()
            await asyncio.sleep(self.__interval_between_jobs)
