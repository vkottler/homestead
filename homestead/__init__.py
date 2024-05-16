"""
A module implementing a raspberry pi synchronous task.
"""

# internal
from runtimepy.net.arbiter import AppInfo
from runtimepy.net.arbiter.config import ConfigObject
from runtimepy.net.arbiter.task import ArbiterTask, TaskFactory


def pi_config(data: ConfigObject) -> None:
    """Sample config-builder method."""

    # configure ui state to not use psutil stats
    print(data)

    del data


class RaspberryPiTask(ArbiterTask):
    """A base raspberry pi housekeeping task."""

    async def init(self, app: AppInfo) -> None:
        """Initialize this task with application information."""

        await super().init(app)

        self.logger.info("Initialized.")

    async def dispatch(self) -> bool:
        """Dispatch an iteration of this task."""

        self.logger.info("Dispatched.")

        return True


class RaspberryPi(TaskFactory[RaspberryPiTask]):
    """A TUI application factory."""

    kind = RaspberryPiTask
