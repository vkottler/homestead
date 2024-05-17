"""
TODO.
"""

# built-in
from os import sep
from pathlib import Path
from typing import Iterator, Type, TypeVar, cast

# third-party
import aiofiles

# built-in
from vcorelib import DEFAULT_ENCODING

SYS = Path(sep, "sys")
T = TypeVar("T", bound="SysInstance")


class SysInstance:
    """A base class for any /sys instance."""

    sys_path: list[str] = []

    def __init__(self, path: Path) -> None:
        """Initialize this instance."""

        assert path.is_dir(), path
        self.path = path

    def attr_path(self, *path: str) -> Path:
        """Get a path to an attibute file."""
        candidate = self.path.joinpath(*path)
        assert candidate.is_file(), candidate
        return candidate

    async def read(self, *path: str) -> str:
        """Read the contents of an Attribute file."""
        async with aiofiles.open(self.attr_path(*path), mode="r") as f:
            contents = cast(str, await f.read())
        return contents

    def write(self, data: str, *path: str) -> None:
        """Write data to an attribute file."""

        with open(
            self.attr_path(*path), mode="w", encoding=DEFAULT_ENCODING
        ) as f:
            f.write(data)

    def write_bool(self, value: bool, *path: str) -> None:
        """Write a boolean attribute."""
        self.write("1" if value else "0", *path)

    def write_int(self, value: int, *path: str) -> None:
        """Write an integer attribute."""
        self.write(str(value), *path)

    async def read_bool(self, *path: str) -> bool:
        """Attempt to read a boolean attribute."""

        return await self.read(*path) == "1"

    async def read_int(self, *path: str) -> int:
        """Attempt to read an integer attribute."""

        return int(await self.read(*path))

    @classmethod
    def instances(cls: Type[T], *path: str) -> Iterator[T]:
        """Iterate over instances found at some path."""

        candidate = SYS.joinpath(*cls.sys_path, *path)
        if candidate.is_dir():
            for inst in candidate.iterdir():
                if inst.is_dir():
                    yield cls(inst)
