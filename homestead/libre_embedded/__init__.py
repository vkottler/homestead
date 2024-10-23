"""
A module implementing file-backed struct instances.
"""

# built-in
from pathlib import Path

# third-party
from runtimepy.channel.environment.file import VALUES_FILE
from runtimepy.net.arbiter.struct import TimestampedStruct
from vcorelib.io import ARBITER, JsonObject

# internal
from homestead.util import LIBRE


class LibreEmbeddedStruct(TimestampedStruct):
    """
    A struct base for disk-backed runtime structures. Useful for hot reload
    and reboot / power-outage tolerance.
    """

    base_path = LIBRE.joinpath("runtime")

    instance_dir: Path
    values_path: Path

    disk_values: JsonObject

    final_poll = True

    def add_channels(self) -> None:
        """Add class-specific channels to the environment."""

    def init_env(self) -> None:
        """Initialize this sample environment."""

        super().init_env()

        self.instance_dir = self.base_path.joinpath(
            "structs", type(self).__name__, self.name
        )
        self.instance_dir.mkdir(parents=True, exist_ok=True)

        self.values_path = self.instance_dir.joinpath(VALUES_FILE)

        # Load initial values.
        self.disk_values = self.app.stack.enter_context(
            ARBITER.object_file_context(self.values_path)
        )

        # Finish adding channels.
        self.add_channels()
        self.env.apply(self.disk_values)  # type: ignore

    def poll(self) -> None:
        """Poll this instance and write values to disk."""

        super().poll()
        self.disk_values = self.env.values()  # type: ignore
        ARBITER.encode(self.values_path, self.disk_values)
