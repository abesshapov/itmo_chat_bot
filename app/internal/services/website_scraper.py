"""Website Scraper Service."""

from asyncio import sleep
import asyncio
import os
from app.pkg.logger import get_logger

from app.pkg.clients.minio import MinioClient


from app.internal.repository.postgresql.supported_programms import (
    SupportedProgrammsRepository,
)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import tempfile
from io import BytesIO


class WebsiteScraperService:
    """Website Scraper Service."""

    __logger = get_logger(__name__)
    __minio_client: MinioClient
    __supported_programms_repository: SupportedProgrammsRepository

    def __init__(
        self,
        minio_client: MinioClient,
        supported_programms_repository: SupportedProgrammsRepository,
    ):

        self.__minio_client = minio_client
        self.__supported_programms_repository = supported_programms_repository

    async def scrap_websites(
        self,
    ) -> None:

        """Scrap websites of all supported programs."""

        self.__logger.info("Starting website scraping for all supported programs.")
        supported_programs = await self.__supported_programms_repository.read_all()
        for program in supported_programs:
            self.__logger.info(
                "Scraping website for program: %s (%s)",
                program.name,
                program.website_url,
            )
            await self.__website_scraping(
                program_name=program.name,
                website_url=program.website_url,
            )

    async def __website_scraping(
        self,
        program_name: str,
        website_url: str,
    ) -> None:
        """Scrap a single website."""

        try:
            folder = tempfile.mkdtemp()
            self.__logger.info("Temporary folder created at: %s", folder)
            options = Options()
            options.set_preference("browser.download.folderList", 2)
            options.set_preference("browser.download.dir", folder)
            # options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            driver = webdriver.Firefox(options=options)
            driver.set_page_load_timeout(600)
            driver.set_script_timeout(600)

            driver.get(website_url)
            element = WebDriverWait(driver, 30).until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//div[contains(@class, 'StudyPlan')]//button[@class='ButtonSimple_button__JbIQ5 ButtonSimple_button_masterProgram__JK8b_']",  # pylint: disable=line-too-long
                    ),
                ),
            )
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                element,
            )
            await asyncio.sleep(3)
            element.click()
            while len(os.listdir(folder)) == 0:
                self.__logger.info("Waiting for download to complete...")
                sleep(5)
            files = os.listdir(folder)
            file = os.path.join(folder, files[0])
            with open(file, "rb") as f:
                file_data = f.read()
            file_data = BytesIO(file_data)
            file_data.seek(0)
            await self.__minio_client.upload_file_to_bucket(
                filename=f"{program_name}.pdf",
                file=file_data,
            )
        except Exception:  # pylint: disable=broad-exception-caught
            self.__logger.exception(
                "Error occurred while scraping website for program: %s (%s)",
                program_name,
                website_url,
            )
        finally:
            driver.close()
            driver.quit()
