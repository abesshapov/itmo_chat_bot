"""Module SecretBytes."""
from pydantic import SecretBytes

from app.internal.pkg.password import crypt_password

__all__ = ["EncryptedSecretBytes"]


class EncryptedSecretBytes(SecretBytes):
    """Model for verify bytes range [6;256] and crypt than by bcrypt
    algorithm."""

    min_length = 6
    max_length = 256

    def crypt_password(self) -> None:
        self._secret_value = crypt_password(self)
