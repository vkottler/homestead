"""
A module implementing interfaces related to Raspberry Pi on-screen keyboards.
"""

# built-in
from os import kill
from signal import Signals

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Bool


async def setup_keyboard_toggle(env: ChannelEnvironment, pid: int) -> None:
    """Set up on-screen keyboard toggling for wvkbd."""

    prim = Bool()
    env.bool_channel("keyboard", kind=prim, commandable=True)

    def keyboard_handler(_: bool, curr: bool) -> None:
        """Handle sending the keyboard-toggle signal."""
        kill(pid, Signals["SIGUSR2" if curr else "SIGUSR1"])

    # Add handler.
    prim.register_callback(keyboard_handler)
