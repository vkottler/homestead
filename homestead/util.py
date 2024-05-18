"""
A module implementing generic runtime-configuration utilities.
"""

# built-in
from os import sep
from pathlib import Path
from typing import cast

# third-party
import aiofiles

# internal
from runtimepy.net.arbiter.config import ConfigObject
from vcorelib import DEFAULT_ENCODING

ROOT = Path(sep)
SYS = ROOT.joinpath("sys")
PROC = ROOT.joinpath("proc")


def disable_ui_psutil(data: ConfigObject) -> None:
    """Disable UI struct's system metrics (we're bringing our own)."""

    for struct in data.get("structs", []):
        if struct["name"] == "ui":
            struct_cfg = struct.setdefault("config", {})
            struct_cfg["psutil"] = False


def read_str(path: Path) -> str:
    """Read file contents as a string."""

    with path.open("r", encoding=DEFAULT_ENCODING) as f:
        contents = f.read()
    return contents


async def aread_str(path: Path) -> str:
    """Read String file contents."""

    async with aiofiles.open(path, mode="r") as f:
        contents = cast(str, await f.read())
    return contents


class AsyncPollable:
    """A simple class declaring a 'poll' interface."""

    async def poll(self) -> None:
        """Poll this instance."""
