"""
A module implementing interfaces for interacting with process identifiers.
"""

# built-in
from asyncio.subprocess import PIPE
from typing import Optional

# third-party
from vcorelib.asyncio.cli import run_command
from vcorelib.logging import LoggerType


async def pgrep(
    logger: LoggerType, pattern: str, entry: str = "pgrep"
) -> Optional[int]:
    """Attempt to get a process ID using pgrep."""

    pid = None

    result = await run_command(logger, entry, pattern, stdout=PIPE)
    if result.stdout:
        pid = int(result.stdout.decode().rstrip())

    return pid
