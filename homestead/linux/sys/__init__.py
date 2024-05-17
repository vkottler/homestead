"""
A module implementing interfaces for interacting with Linux /sys interfaces.

https://www.kernel.org/doc/Documentation/filesystems/sysfs.txt
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Uint8

# internal
from homestead.linux.sys.instance import SysInstance


class SysClass(SysInstance):
    """A class for Linux devices under /sys/class."""

    sys_path = ["class"]


class Backlight(SysClass):
    """A class for Linux backlight devices."""

    sys_path = SysClass.sys_path + ["backlight"]

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment for backlight control."""

        # enter namespace for inst name

        # Setup 'bl_power'.
        # name = "bl_power"
        # prim = Bool(value=await self.read_bool(name))
        # env.bool_channel(name, kind=prim, commandable=True)
        #
        # def bl_power_handler(_: bool, curr: bool) -> None:
        #     """Handle setting the 'bl_power' attribute."""
        #     self.write_bool(curr, name)
        #
        # prim.register_callback(bl_power_handler)

        # How should this be used?
        # max_brightness = 255
        # print(await self.read_int("max_brightness"))

        # Setup 'brightness'.
        name = "brightness"
        brightness = Uint8(value=await self.read_int(name))
        env.int_channel(name, kind=brightness, commandable=True)

        def brightness_handler(_: int, curr: int) -> None:
            """Handle setting the 'brightness' attribute."""
            self.write_int(curr, name)

        brightness.register_callback(brightness_handler)
