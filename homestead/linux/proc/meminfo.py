"""
A module implementing an interface for parsing /proc/meminfo.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from vcorelib.logging import LoggerType

# internal
from homestead.linux.proc.file import ProcFile


class Meminfo(ProcFile):
    """A class implementing an interface for /proc/meminfo."""

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment with this instance."""

        # Create channels.
        del env

    async def poll(self) -> None:
        """Poll this instance."""

        # Parse contents.
        for line in await self.lines():
            del line


async def setup_meminfo(
    logger: LoggerType, env: ChannelEnvironment
) -> Meminfo:
    """Create an uptime instance."""

    result = Meminfo(logger, "meminfo")
    await result.init_env(env)
    return result
