"""
A module implementing an interface for using /proc/loadavg data at runtime.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Float, Uint32
from vcorelib.logging import LoggerType

# internal
from homestead.linux.proc.file import ProcFile


class Loadavg(ProcFile):
    """A class implementing an interface for /proc/loadavg."""

    one_minute: Float
    five_minute: Float
    fifteen_minute: Float

    runnable: Uint32
    total: Uint32

    newest_pid: Uint32

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment for backlight control."""

        with env.names_pushed("loadavg"):
            self.one_minute = Float()
            env.float_channel("1m", kind=self.one_minute)
            self.five_minute = Float()
            env.float_channel("5m", kind=self.five_minute)
            self.fifteen_minute = Float()
            env.float_channel("15m", kind=self.fifteen_minute)

            self.runnable = Uint32()
            env.int_channel("runnable", kind=self.runnable)
            self.total = Uint32()
            env.int_channel("total", kind=self.total)

            self.newest_pid = Uint32()
            env.int_channel("newest_pid", kind=self.newest_pid)

    async def poll(self) -> None:
        """Poll this instance."""

        data = (await self.aread()).rstrip().split()
        if len(data) >= 5:
            self.one_minute.value = float(data[0])
            self.five_minute.value = float(data[1])
            self.fifteen_minute.value = float(data[2])

            runnable, total = data[3].split("/")
            self.runnable.value = int(runnable)
            self.total.value = int(total)

            self.newest_pid.value = int(data[4])


async def setup_loadavg(
    logger: LoggerType, env: ChannelEnvironment
) -> Loadavg:
    """Create a loadavg interface."""

    result = Loadavg(logger, "loadavg")
    await result.init_env(env)
    return result
