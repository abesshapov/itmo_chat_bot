"""All connectors in declarative container."""

from dependency_injector import containers, providers

from app.pkg.connectors.postgresql import PostgresSQL
from app.pkg.connectors.redis import Redis

__all__ = ["Connectors", "PostgresSQL", "Redis"]


class Connectors(containers.DeclarativeContainer):
    """Declarative container with all connectors."""

    postgresql: PostgresSQL = providers.Container(PostgresSQL)

    redis: Redis = providers.Container(Redis)
