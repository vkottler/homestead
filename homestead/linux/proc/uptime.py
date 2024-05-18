"""
A module implementing an interface for using /proc/uptime data at runtime.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Float
from vcorelib.logging import LoggerType

# internal
from homestead.linux.proc.file import ProcFile


class Uptime(ProcFile):
    """A class implementing an interface for /proc/uptime."""

    uptime: Float

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment with this instance."""

        self.uptime = Float()
        env.float_channel("uptime", kind=self.uptime)

    async def poll(self) -> None:
        """Poll this instance."""
        self.uptime.value = float((await self.aread()).rstrip().split()[0])


async def setup_uptime(logger: LoggerType, env: ChannelEnvironment) -> Uptime:
    """Create an uptime instance."""

    result = Uptime(logger, "uptime")
    await result.init_env(env)
    return result
