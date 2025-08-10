"""Create connection to redis."""

from contextlib import asynccontextmanager
from typing import Union

import redis.asyncio
import redis.asyncio.client
from dependency_injector.wiring import Provide, inject

from app.pkg.connectors import Connectors

__all__ = ["get_connection", "acquire_connection"]


@asynccontextmanager
@inject
async def get_connection(
    pool: redis.asyncio.Redis = Provide[Connectors.redis.connector],
    return_pool: bool = False,
) -> Union[redis.asyncio.Redis, redis.asyncio.client.Pipeline]:  # type: ignore
    """Get async connection pool to redis.

    Args:
        pool:
            redis connection pool.
        return_pool:
            if True, return pool, else return connection.

    Examples:
        If you have a function that contains a query in redis,
        context manager :func:`.get_connection`
        will get async connection to redis
        of pool::

            >>> async def exec_some_sql_function() -> None:
            ...     async with get_connection() as c:
            ...         await c.execute("SELECT * FROM users")

    Returns:
        Async connection to redis.
    """
    if not isinstance(pool, redis.asyncio.Redis):
        pool = await pool

    if return_pool:
        yield pool
        return

    async with acquire_connection(pool) as channel:
        yield channel


@asynccontextmanager
async def acquire_connection(
    pool: redis.asyncio.Redis,
) -> redis.asyncio.client.Pipeline:  # type: ignore
    """Acquire connection from pool.

    Args:
        pool:
            Settings from :func:`.get_connection` redis pool.

    Examples:
        If you have a function that contains a query in rabbitmq,
        context manager :func:`.acquire_connection`
        will get async connection to redis
        of pool

    Returns:
        Async connection to redis.
    """
    async with pool.pipeline(transaction=True) as connection:
        yield connection
