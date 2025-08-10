"""
user specifics table
"""

from yoyo import step

__depends__ = {'20250810_01_PvLuI-added-supported-programms-table'}

steps = [
    step(
        """
create table if not exists user_specifics (
    user_id numeric,
    specific text not null
);
        """,
        """
drop table if exists user_specifics;
        """
    ),
]
