"""
A module implementing a Linux housekeeping task.
"""

# built-in
import asyncio
import os
from pathlib import Path

# third-party
from runtimepy.mixins.logging import LogCaptureMixin
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory

# internal
from homestead.linux.keyboard import setup_keyboard_toggle
from homestead.linux.proc.loadavg import setup_loadavg
from homestead.linux.proc.stat import setup_stat
from homestead.linux.proc.uptime import setup_uptime
from homestead.linux.sys.backlight import setup_backlight_controllers
from homestead.linux.sys.thermal import setup_thermal_controllers
from homestead.util import AsyncPollable


class LinuxTask(ArbiterTask, LogCaptureMixin):
    """A base raspberry pi housekeeping task."""

    to_poll: list[AsyncPollable]

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)
        self.to_poll = []

        # Register Linux integrations.
        await setup_keyboard_toggle(self.logger, self.env)
        await setup_backlight_controllers(self.logger, self.env)
        self.to_poll += await setup_thermal_controllers(self.logger, self.env)
        self.to_poll.append(await setup_loadavg(self.logger, self.env))
        self.to_poll.append(await setup_uptime(self.logger, self.env))
        self.to_poll.append(await setup_stat(self.logger, self.env))

        # System log monitoring.
        await self.init_log_capture(
            app.stack, [("info", Path(os.sep, "var", "log", "syslog"))]
        )

        # get current process's stats (config option?)

        # system cpu stats (Stat interface), memory stats? (config option?)

        # network interface stats: /sys/class/net/<inst>/statistics/*

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        # Poll integrations.
        await asyncio.gather(
            self.dispatch_log_capture(), *(x.poll() for x in self.to_poll)
        )

        return True


class Linux(TaskFactory[LinuxTask]):
    """A Linux task factory."""

    kind = LinuxTask
