"""
A module implementing a sys-instance interface for thermal devices.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Float

# internal
from homestead.linux.sys.instance import SysClass


def raw_to_fahrenheit(raw: int) -> float:
    """Convert a raw measurement (milli-Celsius) to Fahrenheit."""
    return ((raw / 1000) * 9 / 5) + 32


class Thermal(SysClass):
    """A class for Linux backlight devices."""

    sys_path = SysClass.sys_path + ["thermal"]
    temp: Float

    async def raw_temp(self) -> int:
        """Get a raw temperature reading."""
        return await self.read_int("temp")

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment for backlight control."""

        with env.names_pushed(self.path.name):
            # enum for unit (commandable)?
            self.temp = Float(value=raw_to_fahrenheit(await self.raw_temp()))
            env.float_channel("temp", kind=self.temp)

    async def poll(self) -> None:
        """Poll this instance."""

        self.temp.value = raw_to_fahrenheit(await self.raw_temp())


async def setup_thermal_controllers(env: ChannelEnvironment) -> list[Thermal]:
    """Check for backlight devices."""

    result = []

    for inst in Thermal.instances(kind="cpu-thermal"):
        await inst.init_env(env)
        result.append(inst)

    return result
