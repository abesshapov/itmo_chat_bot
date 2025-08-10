"""User specifics repository."""

from typing import List
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.postgresql.handlers.collect_response import (
    collect_response,
)
from app.internal.repository.repository import Repository
from app.pkg.models.app.user_specific import repository


class UserSpecificsRepository(Repository):
    """User specifics repository."""

    @collect_response
    async def create(
        self,
        cmd: repository.CreateUserSpecificCommand,
    ) -> repository.UserSpecificResponse:
        """Create user specific."""

        q = """
            insert into user_specifics (user_id, specific)
            values (%(user_id)s, %(specific)s)
            returning user_id, specific;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    @collect_response
    async def read_listed(
        self,
        cmd: repository.ReadUserSpecificCommand,
    ) -> List[repository.UserSpecificResponse]:
        """Read user specifics by user ID."""

        q = """
            select
                user_id,
                specific
            from user_specifics
            where user_id = %(user_id)s
            order by specific;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchall()

    @collect_response
    async def read_all(
        self,
    ) -> List[repository.UserSpecificResponse]:
        """Read all user specifics."""

        q = """
            select
                user_id,
                specific
            from user_specifics
            order by user_id;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()
