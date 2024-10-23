"""
A module implementing various dummy interfaces.
"""

# internal
from homestead.libre_embedded import LibreEmbeddedStruct


class NullStruct(LibreEmbeddedStruct):
    """A sample struct."""

    def add_channels(self) -> None:
        """Add class-specific channels to the environment."""

        self.env.int_channel(
            "null.int", commandable=True, description="A sample integer."
        )
        self.env.bool_channel(
            "null.bool", commandable=True, description="A sample boolean."
        )
        self.env.float_channel(
            "null.float",
            commandable=True,
            description="A sample floating-point number.",
        )
