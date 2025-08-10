"""Container with Redis connector."""

from dependency_injector import containers, providers

from app.pkg.connectors.redis import resource
from app.pkg.settings import settings


class Redis(containers.DeclarativeContainer):
    """Declarative container with Redis connector."""

    configuration = providers.Configuration(
        name="settings",
        pydantic_settings=[settings.REDIS],
    )

    connector: resource.Redis = providers.Resource(
        resource.Redis,
        dsn=configuration.DSN,
        max_connections=configuration.MAX_CONNECTION,
    )
