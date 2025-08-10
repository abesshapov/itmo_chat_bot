"""All postgresql repositories are defined here."""

from dependency_injector import containers, providers

from app.internal.repository.postgresql.supported_programms import (
    SupportedProgrammsRepository,
)
from app.internal.repository.postgresql.user_specifics import UserSpecificsRepository


class Repositories(containers.DeclarativeContainer):
    """Container for postgresql repositories."""

    supported_programms_repository = providers.Singleton(
        SupportedProgrammsRepository,
    )

    user_specifics_repository = providers.Singleton(
        UserSpecificsRepository,
    )
