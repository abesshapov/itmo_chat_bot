"""Supported programms service."""

from logging import Logger
from app.pkg.logger import get_logger

from app.internal.repository.postgresql.supported_programms import (
    SupportedProgrammsRepository,
)

from app.pkg.models.app.supported_program import (
    repository as supported_program_repository,
)
from app.pkg.models.exceptions.repository import EmptyResult


class SupportedProgrammsService:
    """Service for supported programms."""

    __logger: Logger = get_logger(__name__)
    __supported_programms_repository: SupportedProgrammsRepository

    def __init__(self, supported_programms_repository: SupportedProgrammsRepository):
        self.__supported_programms_repository = supported_programms_repository

    async def get_programs(
        self,
    ) -> list[supported_program_repository.SupportedProgramResponse]:
        """Get all supported programs."""

        self.__logger.info("Fetching all supported programs.")
        try:
            return await self.__supported_programms_repository.read_all()
        except EmptyResult:
            return []
