"""
A module implementing generic runtime-configuration utilities.
"""

# built-in
from os import sep
from pathlib import Path

# internal
from runtimepy.net.arbiter.config import ConfigObject
from runtimepy.net.server import RuntimepyServerConnection
from runtimepy.util import read_binary
from vcorelib import DEFAULT_ENCODING

ROOT = Path(sep)
SYS = ROOT.joinpath("sys")
PROC = ROOT.joinpath("proc")
LIBRE_STR = "libre-embedded"
LIBRE = ROOT.joinpath("opt", LIBRE_STR)


def libre_repo_path(
    repo: str, owner: str = LIBRE_STR, strict: bool = True
) -> Path:
    """Locate a source repository path."""

    result = LIBRE.joinpath("src", owner, repo)
    if strict:
        assert result.is_dir(), result

    return result


def disable_ui_psutil(data: ConfigObject) -> None:
    """Disable UI struct's system metrics (we're bringing our own)."""

    for struct in data.get("structs", []):
        if struct["name"] == "ui":
            struct_cfg = struct.setdefault("config", {})
            struct_cfg["psutil"] = False


def add_web_server_paths(_: ConfigObject) -> None:
    """Add some disk paths to runtimepy's HTTP server."""

    # Add markdown sources.
    path = libre_repo_path(".github").joinpath("md")
    if path not in RuntimepyServerConnection.class_paths:
        RuntimepyServerConnection.class_paths.append(path)


def read_str(path: Path) -> str:
    """Read file contents as a string."""

    with path.open("r", encoding=DEFAULT_ENCODING) as f:
        contents = f.read()
    return contents


async def aread_str(path: Path) -> str:
    """Read String file contents."""
    return (await read_binary(path)).decode()


class AsyncPollable:
    """A simple class declaring a 'poll' interface."""

    async def poll(self) -> None:
        """Poll this instance."""
