"""Supported programms repository."""

from typing import List
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.postgresql.handlers.collect_response import (
    collect_response,
)
from app.internal.repository.repository import Repository
from app.pkg.models.app.supported_program import repository


class SupportedProgrammsRepository(Repository):
    """Supported programms repository."""

    @collect_response
    async def read_all(
        self,
    ) -> List[repository.SupportedProgramResponse]:
        """Read all supported programms."""

        q = """
            select
                id,
                name,
                website_url
            from supported_programms
            order by name;
        """
        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()
