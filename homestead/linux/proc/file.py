"""
A module implementing a base /proc file interface.
"""

# third-party
from vcorelib.logging import LoggerMixin, LoggerType

# internal
from homestead.util import PROC, AsyncPollable, aread_str


class ProcFile(LoggerMixin, AsyncPollable):
    """An interface for reading files under /proc."""

    def __init__(self, logger: LoggerType, *path: str) -> None:
        """Initialize this instance."""

        candidate = PROC.joinpath(*path)
        assert candidate.is_file(), candidate
        self.path = candidate
        super().__init__(logger=logger)

    async def aread(self) -> str:
        """Read the contents of an Attribute file."""
        return await aread_str(self.path)
