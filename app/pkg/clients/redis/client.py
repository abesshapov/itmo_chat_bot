"""Redis client abstraction."""

from logging import Logger
from typing import List

from app.pkg.connectors.redis.connection import get_connection
from app.pkg.logger import get_logger


class RedisClient:
    """Redis client abstraction."""

    __logger: Logger = get_logger(__name__)

    async def hmset(self, key: str, value: dict):
        async with get_connection() as connection:
            return await connection.hset(key, mapping=value).execute()

    async def hgetall(self, key: str):
        async with get_connection() as connection:
            return await connection.hgetall(key).execute()

    async def hdel(self, key: str, fields: List[str]):
        async with get_connection() as connection:
            for field in fields:
                await connection.hdel(key, field)
            return await connection.execute()

    async def delete(self, key: str):
        async with get_connection() as connection:
            return await connection.delete(key).execute()
