"""
A module implementing a raspberry pi synchronous task.
"""

# built-in
from asyncio.subprocess import PIPE
from os import sep
from pathlib import Path
from typing import Optional

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory
from vcorelib.asyncio.cli import run_command

# internal
from homestead.pi.keyboard import setup_keyboard_toggle

SYS = Path(sep, "sys")
SYS_CLASS = SYS.joinpath("class")


class RaspberryPiTask(ArbiterTask):
    """A base raspberry pi housekeeping task."""

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        # Look for on-screen keyboard process to send signals to.
        wvkbd_pid = await self.pgrep("wvkbd")
        if wvkbd_pid:
            await setup_keyboard_toggle(self.env, wvkbd_pid)

        # Check for backlight devices.
        path = SYS_CLASS.joinpath("backlight")
        print(path)

    async def pgrep(self, pattern: str, entry: str = "pgrep") -> Optional[int]:
        """Attempt to get a process ID using pgrep."""

        pid = None

        result = await run_command(self.logger, entry, pattern, stdout=PIPE)
        if result.stdout:
            pid = int(result.stdout.decode().strip())

        return pid

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # self.logger.info("Dispatched.")

        return True


class RaspberryPi(TaskFactory[RaspberryPiTask]):
    """A TUI application factory."""

    kind = RaspberryPiTask
