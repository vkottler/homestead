"""
A module implementing a raspberry pi synchronous task.
"""

# built-in
from os import sep
from pathlib import Path

# internal
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory

SYS = Path(sep, "sys")
SYS_CLASS = SYS.joinpath("class")


class RaspberryPiTask(ArbiterTask):
    """A base raspberry pi housekeeping task."""

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        # Check for backlight devices.
        path = SYS_CLASS.joinpath("backlight")
        print(path)

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        self.logger.info("Dispatched.")

        return True


class RaspberryPi(TaskFactory[RaspberryPiTask]):
    """A TUI application factory."""

    kind = RaspberryPiTask
