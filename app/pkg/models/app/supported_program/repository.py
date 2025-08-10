"""Supported program repository models."""

from app.pkg.models.app.supported_program import SupportedProgramFields


class SupportedProgramResponse(
    SupportedProgramFields.Identifiers,
    SupportedProgramFields.Name,
    SupportedProgramFields.WebsiteUrl,
):
    """Response model for supported program."""
