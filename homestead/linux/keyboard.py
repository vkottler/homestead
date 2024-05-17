"""
A module implementing interfaces related to on-screen keyboards for Linux.
"""

# built-in
from os import kill
from signal import Signals

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Bool
from vcorelib.logging import LoggerType

# internal
from homestead.linux.pid import pgrep


async def setup_keyboard_toggle(
    logger: LoggerType, env: ChannelEnvironment, wvkbd: str = "wvkbd"
) -> None:
    """Set up on-screen keyboard toggling for wvkbd."""

    # Look for on-screen keyboard process to send signals to.
    pid = await pgrep(logger, wvkbd)
    if pid:
        prim = Bool()
        env.bool_channel("keyboard", kind=prim, commandable=True)

        def keyboard_handler(_: bool, curr: bool) -> None:
            """Handle sending the keyboard-toggle signal."""
            kill(pid, Signals["SIGUSR2" if curr else "SIGUSR1"])

        # Add handler.
        prim.register_callback(keyboard_handler)
