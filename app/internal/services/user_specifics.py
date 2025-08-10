"""User specifics service."""

from logging import Logger
from app.pkg.logger import get_logger

from app.internal.repository.postgresql.user_specifics import UserSpecificsRepository

from app.pkg.models.app.user_specific import repository as user_specific_repository
from app.pkg.models.exceptions.repository import EmptyResult


class UserSpecificsService:
    """Service for user specifics."""

    __logger: Logger = get_logger(__name__)
    __user_specifics_repository: UserSpecificsRepository

    def __init__(self, user_specifics_repository: UserSpecificsRepository):
        self.__user_specifics_repository = user_specifics_repository

    async def create_user_specific(
        self,
        user_id: int,
        specific: str,
    ) -> user_specific_repository.UserSpecificResponse:
        """Create user specific."""

        return await self.__user_specifics_repository.create(
            user_specific_repository.CreateUserSpecificCommand(
                user_id=user_id,
                specific=specific,
            ),
        )

    async def get_user_specifics(
        self,
        user_id: int,
    ) -> list[user_specific_repository.UserSpecificResponse]:
        """Get user specifics by user ID."""

        self.__logger.info("Fetching user specifics for user ID: %s", user_id)
        try:
            return await self.__user_specifics_repository.read_listed(
                user_specific_repository.ReadUserSpecificCommand(user_id=user_id),
            )
        except EmptyResult:
            return []
