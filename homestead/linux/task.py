"""
A module implementing a Linux housekeeping task.
"""

# built-in
import asyncio

# third-party
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory

# internal
from homestead.linux.keyboard import setup_keyboard_toggle
from homestead.linux.sys.backlight import setup_backlight_controllers
from homestead.linux.sys.thermal import setup_thermal_controllers
from homestead.util import AsyncPollable


class LinuxTask(ArbiterTask):
    """A base raspberry pi housekeeping task."""

    to_poll: list[AsyncPollable]

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self.to_poll = []

        # Register Linux integrations.
        await setup_keyboard_toggle(self.logger, self.env)
        await setup_backlight_controllers(self.env)
        self.to_poll += await setup_thermal_controllers(self.env)

        # get current process's stats (config option?)

        # system cpu stats, memory stats? (config option?)

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # Poll integrations.
        await asyncio.gather(*(x.poll() for x in self.to_poll))

        return True


class Linux(TaskFactory[LinuxTask]):
    """A Linux task factory."""

    kind = LinuxTask
