"""
A module implementing interfaces related to backlight controllers for Linux.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment

# internal
from homestead.linux.sys import Backlight


async def setup_backlight_controllers(env: ChannelEnvironment) -> None:
    """Check for backlight devices."""

    for inst in Backlight.instances():
        await inst.init_env(env)
