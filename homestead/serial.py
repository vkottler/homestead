"""
A module interfacing with /dev/serial instances.
"""

# built-in
from pathlib import Path
from typing import Iterator, Optional

# third-party
from runtimepy.net.arbiter.info import AppInfo
from vcorelib.asyncio.cli import run_command

# internal
from mklocal.prompts import manual_select

DEV_SERIAL = Path("/dev/serial")


def serial_by_id() -> Iterator[Path]:
    """Iterate over serial device paths."""

    by_id = DEV_SERIAL.joinpath("by-id")
    if by_id.is_dir():
        yield from by_id.iterdir()


def select_serial_port(**kwargs) -> Optional[Path]:
    """Attempt to select a serial port."""

    paths = {x.name: x for x in serial_by_id()}

    result = None
    selection = manual_select("serial port", list(paths), **kwargs)
    if selection:
        result = paths[selection]

    return result


async def tio(app: AppInfo) -> int:
    """Run tio with the selected serial port."""

    # Open tio.
    port = select_serial_port()
    if port:
        await run_command(app.logger, "tio", str(port))

    return 0
