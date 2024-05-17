"""
A module implementing a Linux housekeeping task.
"""

# built-in
from os import sep
from pathlib import Path

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory

# internal
from homestead.linux.backlight import setup_backlight_controllers
from homestead.linux.keyboard import setup_keyboard_toggle

SYS = Path(sep, "sys")
SYS_CLASS = SYS.joinpath("class")


class LinuxTask(ArbiterTask):
    """A base raspberry pi housekeeping task."""

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        # Register Linux integrations.
        await setup_keyboard_toggle(self.logger, self.env)
        await setup_backlight_controllers(self.env)

        # cpu stats, memory stats

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # self.logger.info("Dispatched.")

        return True


class Linux(TaskFactory[LinuxTask]):
    """A Linux task factory."""

    kind = LinuxTask
