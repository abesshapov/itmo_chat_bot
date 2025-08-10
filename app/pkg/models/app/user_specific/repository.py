"""User specific repository models."""

from app.pkg.models.app.user_specific import UserSpecificFields


class CreateUserSpecificCommand(
    UserSpecificFields.UserId,
    UserSpecificFields.Specific,
):
    """Command to create user specific data."""


class ReadUserSpecificCommand(
    UserSpecificFields.UserId,
):
    """Command to read user specific data."""


class UserSpecificResponse(
    UserSpecificFields.UserId,
    UserSpecificFields.Specific,
):
    """Response model for user specific data."""
