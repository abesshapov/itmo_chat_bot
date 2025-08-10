"""Module for load settings form `.env` or if server running with parameter
`dev` from `.env.dev`"""


import typing
import urllib.parse
from functools import lru_cache

from dotenv import find_dotenv
from pydantic import (
    AnyUrl,
    NonNegativeInt,
    PostgresDsn,
    RedisDsn,
    root_validator,
)
from pydantic.env_settings import BaseSettings
from pydantic.types import PositiveInt, SecretStr

from app.pkg.models.core.logger import LoggerLevel

__all__ = ["Settings", "get_settings"]


class _Settings(BaseSettings):
    """Base settings for all settings.

    Use double underscore for nested env variables.

    Examples:
        `.env` file should look like::

            TELEGRAM__TOKEN=...
            TELEGRAM__WEBHOOK_DOMAIN_URL=...

            LOGGER__PATH_TO_LOG="./src/logs"
            LOGGER__LEVEL="DEBUG"

            API_SERVER__HOST="127.0.0.1"
            API_SERVER__PORT=9191

    Warnings:
        In the case where a value is specified for the same Settings field in multiple
        ways, the selected value is determined as follows
        (in descending order of priority):

        1. Arguments passed to the Settings class initializer.
        2. Environment variables, e.g., my_prefix_special_function as described above.
        3. Variables loaded from a dotenv (.env) file.
        4. Variables loaded from the secrets directory.
        5. The default field values for the Settings model.

    See Also:
        https://docs.pydantic.dev/latest/usage/pydantic_settings/
    """

    class Config:
        """Configuration of settings."""

        #: str: env file encoding.
        env_file_encoding = "utf-8"
        #: str: allow custom fields in model.
        arbitrary_types_allowed = True
        #: bool: case-sensitive for env variables.
        case_sensitive = True
        #: str: delimiter for nested env variables.
        env_nested_delimiter = "__"
        #: str: allow extra fields.
        extra = "ignore"


class Postgresql(_Settings):
    """Postgresql settings."""

    #: str: Postgresql host.
    HOST: str = "localhost"
    #: PositiveInt: positive int (x > 0) port of postgresql.
    PORT: PositiveInt = 5432
    #: str: Postgresql user.
    USER: str = "postgres"
    #: SecretStr: Postgresql password.
    PASSWORD: SecretStr = SecretStr("postgres")
    #: str: Postgresql database name.
    DATABASE_NAME: str = "postgres"

    #: PositiveInt: Min count of connections in one pool to postgresql.
    MIN_CONNECTION: PositiveInt = 1
    #: PositiveInt: Max count of connections in one pool  to postgresql.
    MAX_CONNECTION: PositiveInt = 16

    #: str: Concatenation all settings for postgresql in one string. (DSN)
    #  Builds in `root_validator` method.
    DSN: typing.Optional[str] = None

    @root_validator(pre=True)
    def build_dsn(cls, values: dict):  # pylint: disable=no-self-argument
        """Build DSN for postgresql.

        Args:
            values: dict with all settings.

        Notes:
            This method is called before any other validation.
            I use it to build DSN for postgresql.

        See Also:
            About validators:
                https://pydantic-docs.helpmanual.io/usage/validators/#root-validators

            About DSN:
                https://pydantic-docs.helpmanual.io/usage/types/#postgresdsn

        Returns:
            dict with all settings and DSN.
        """

        values["DSN"] = PostgresDsn.build(
            scheme="postgresql",
            user=f"{values.get('USER')}",
            password=f"{urllib.parse.quote_plus(values.get('PASSWORD'))}",
            host=f"{values.get('HOST')}",
            port=f"{values.get('PORT')}",
            path=f"/{values.get('DATABASE_NAME')}",
        )
        return values


class Redis(_Settings):
    """Redis settings."""

    #: str: Redis host.
    HOST: str = "localhost"
    #: PositiveInt: positive int (x > 0) port of Redis.
    PORT: PositiveInt = 6379
    #: str: Redis user.
    USER: typing.Optional[str] = None
    #: SecretStr: Redis password.
    PASSWORD: SecretStr = SecretStr("redis")
    #: str: Redis database name.
    PATH: NonNegativeInt = 1
    #: PositiveInt: Max count of connections in one pool to cache.
    MAX_CONNECTION: PositiveInt = 5

    #: str: Concatenation all settings for cache in one string. (DSN)
    #  Builds in `root_validator` method.
    DSN: typing.Optional[str] = None

    @root_validator(pre=True)
    def build_dsn(cls, values: dict):  # pylint: disable=no-self-argument
        """Build DSN for cache.

        Args:
            values: dict with all settings.

        Notes:
            This method is called before any other validation.
            I use it to build DSN for cache.

        See Also:
            About validators:
                https://pydantic-docs.helpmanual.io/usage/validators/#root-validators

            About DSN:
                https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.RedisDsn

        Returns:
            dict with all settings and DSN.
        """

        values["DSN"] = RedisDsn.build(
            scheme="redis",
            user=f"{values.get('USER', '')}",
            password=f"{urllib.parse.quote_plus(values.get('PASSWORD'))}",
            host=f"{values.get('HOST')}",
            port=f"{values.get('PORT')}",
            path=f"/{values.get('PATH')}",
        )
        return values


class S3(_Settings):
    """S3 settings."""

    #: str: S3 bucket name.
    BUCKET_NAME: str

    #: SecretStr: S3 root user
    ROOT_USER: SecretStr

    #: SecretStr: S3 root password
    ROOT_PASSWORD: SecretStr

    #: str: S3 host
    HOST: str

    #: PositiveInt: S3 port
    PORT: PositiveInt


class OpenAI(_Settings):
    """OpenAI settings."""

    #: str: OpenAI API key.
    API_KEY: SecretStr

    #: str: Model name.
    MODEL_NAME: str = "gpt-4o-search-preview"


class Telegram(_Settings):
    """Telegram settings."""

    BOT_TOKEN: SecretStr

    BOT_WEBHOOK_URL: AnyUrl

    BOT_WEBHOOK_PATH: str

    SECRET_TOKEN: SecretStr


class Logging(_Settings):
    """Logging settings."""

    #: StrictStr: Level of logging which outs in std
    LEVEL: LoggerLevel = LoggerLevel.DEBUG


class APIServer(_Settings):
    """API settings."""

    # --- API SETTINGS ---
    #: str: Name of API service
    INSTANCE_APP_NAME: str = "project_name"
    #: str: API host.
    HOST: str = "localhost"
    #: PositiveInt: positive int (x > 0) port of API.
    PORT: PositiveInt = 5000
    # --- OTHER SETTINGS ---
    #: Logging: Logging settings.
    LOGGER: Logging


class Settings(_Settings):
    """Server settings.

    Formed from `.env` or `.env.dev` if server running with parameter
    `dev`.
    """

    #: APIServer: API settings. Contains all settings for API.
    API: APIServer

    #: Postgresql: Postgresql settings.
    POSTGRES: Postgresql

    #: Redis: Redis settings.
    REDIS: Redis

    #: Telegram: Telegram settings.
    TELEGRAM: Telegram

    #: S3: S3 settings.
    S3: S3

    #: OpenAI: OpenAI settings.
    OPENAI: OpenAI


@lru_cache
def get_settings(env_file: str = ".env") -> Settings:
    """Create settings instance."""

    return Settings(_env_file=find_dotenv(env_file))
