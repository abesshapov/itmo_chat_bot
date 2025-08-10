"""Async resource for Redis connector."""
import asyncio

import redis.asyncio

from app.pkg.connectors.resources import BaseAsyncResource


class Redis(BaseAsyncResource):
    """Redis connector using aioredis."""

    async def init(self, dsn: str, *args, **kwargs) -> redis.asyncio.Redis:
        """Getting connection pool in asynchronous.

        Args:
            dsn: D.S.N - Data Source Name.

        Returns:
            Created connection pool.
        """

        return redis.asyncio.from_url(
            url=dsn,
            **kwargs,
        )

    async def shutdown(self, resource: redis.asyncio.Redis):
        """Close connection.

        Args:
            resource: Resource returned by :meth:`.Redis.from_url()` method.

        Notes:
            This method is called automatically
            when the application is stopped
            or
            ``Closing`` provider is used.
        """
        if isinstance(resource, asyncio.Task):
            resource = await resource

        await resource.aclose()
