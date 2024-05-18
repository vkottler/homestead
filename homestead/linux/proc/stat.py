"""
A module implementing an interface for using /proc/stat data at runtime.
"""

# third-party
from runtimepy.channel.environment import ChannelEnvironment
from runtimepy.primitives import Float
from vcorelib.logging import LoggerType

# internal
from homestead.linux.proc.file import ProcFile


class Stat(ProcFile):
    """A class implementing an interface for /proc/stat."""

    idle_count: dict[str, int]
    non_idle_count: dict[str, int]

    # man 5 proc
    non_idle_idx = [1, 2, 3, 5, 6, 7, 8, 9, 10]

    util: dict[str, Float]

    async def init_env(self, env: ChannelEnvironment) -> None:
        """Initialize a channel environment with this instance."""

        self.idle_count = {}
        self.non_idle_count = {}

        # https://stackoverflow.com/a/54001819
        # getconf CLK_TCK

        # Set up CPU utilization channels.
        self.util = {}
        for line in await self.lines():
            parts = line.split()
            label = parts[0]
            if label.startswith("cpu"):
                self.util[label] = Float()
                with env.names_pushed(label):
                    env.float_channel("percent", kind=self.util[label])

    def update_counts(self, line: list[str]) -> None:
        """Update CPU utilization tracking."""

        cpu = line[0]

        # Load from previous iteration.
        prev_idle = self.idle_count.setdefault(cpu, 0)
        prev_non_idle = self.non_idle_count.setdefault(cpu, 0)

        # Calculate new non-idle proportion.
        non_idle = 0
        for idx in self.non_idle_idx:
            non_idle += int(line[idx])
        self.non_idle_count[cpu] = non_idle

        # Calculate idle proportion.
        idle = int(line[4])
        self.idle_count[cpu] = idle

        idle_change = idle - prev_idle
        non_idle_change = non_idle - prev_non_idle

        # Rolling average at some point?
        total = idle_change + non_idle_change
        if total:
            self.util[cpu].value = (non_idle_change / total) * 100

    async def poll(self) -> None:
        """Poll this instance."""

        for line in await self.lines():
            parts = line.split()
            if parts[0].startswith("cpu"):
                self.update_counts(parts)


async def setup_stat(logger: LoggerType, env: ChannelEnvironment) -> Stat:
    """Create an uptime instance."""

    result = Stat(logger, "stat")
    await result.init_env(env)
    return result
