"""Module for crypt and decrypt password."""

from typing import Union

from argon2 import PasswordHasher
from argon2 import exceptions as argon2_exception
from argon2 import low_level
from pydantic.types import SecretBytes, SecretStr

from app.pkg.models.exceptions import auth as auth_exceptions


def crypt_password(password: Union[SecretStr, SecretBytes]) -> SecretBytes:
    """Encrypt password using Argon2id algorithm.

    Args:
        password: Password passed as plain text

    Returns:
        SecretBytes: Hashed password
    """

    ph = PasswordHasher(type=low_level.Type.ID)

    try:
        password_hash = ph.hash(
            password.get_secret_value(),
        ).encode()
    except argon2_exception.HashingError as exc:
        raise auth_exceptions.PasswordHashingError from exc

    return SecretBytes(value=password_hash)


def check_password(password: SecretStr, password_hash: SecretBytes):
    """Check password.

    Args:
        password: Password passed as plain text
        password_hash: Password hash

    Raises
        IncorrectUsernameOrPassword: Incorrect user password
        InvalidHashError: Invalid hash value is given.
                          Server error 'cause hash is invalid
    """

    ph = PasswordHasher(type=low_level.Type.ID)

    try:
        ph.verify(
            hash=password_hash.get_secret_value(),
            password=password.get_secret_value(),
        )
    except argon2_exception.VerificationError as exc:
        raise auth_exceptions.IncorrectUsernameOrPassword from exc
    except argon2_exception.InvalidHashError as exc:
        raise auth_exceptions.InvalidPasswordHashValue from exc
