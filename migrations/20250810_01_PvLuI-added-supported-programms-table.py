"""
added supported programms table
"""

from yoyo import step

__depends__ = {}

steps = [
    step(
        """
create table if not exists supported_programms (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    website_url text not null
);
        """,
        """
drop table if exists supported_programms;
        """
    ),
    step(
        """
insert into supported_programms (name, website_url) values
('Искусственный интеллект', 'https://abit.itmo.ru/program/master/ai'),
('Управление ИИ-продуктами', 'https://abit.itmo.ru/program/master/ai_product');
        """,
        """
delete from supported_programms where name in (
    'Искусственный интеллект',
    'Управление ИИ-продуктами'
);
        """,
    ),
]
