"""
A module implementing an object-oriented interface for /sys attribute reading
and writing.
"""

# built-in
from os import sep
from pathlib import Path
from typing import Iterable, Iterator, Type, TypeVar

# third-party
from vcorelib import DEFAULT_ENCODING
from vcorelib.logging import LoggerMixin, LoggerType

# internal
from homestead.util import AsyncPollable, aread_str, read_str

ROOT = Path(sep)
SYS = ROOT.joinpath("sys")
T = TypeVar("T", bound="SysInstance")


class SysInstance(LoggerMixin, AsyncPollable):
    """A base class for any /sys instance."""

    sys_path: list[str] = []

    def __init__(self, logger: LoggerType, path: Path) -> None:
        """Initialize this instance."""

        assert path.is_dir(), path
        self.path = path
        super().__init__(logger=logger)

    def has_attr(self, *path: str) -> bool:
        """Determine if this instance has a specific attribute file."""
        return self.path.joinpath(*path).is_file()

    def attr_path(self, *path: str) -> Path:
        """Get a path to an attibute file."""
        candidate = self.path.joinpath(*path)
        assert candidate.is_file(), candidate
        return candidate

    async def aread(self, *path: str) -> str:
        """Read the contents of an Attribute file."""
        return await aread_str(self.attr_path(*path))

    def write(self, data: str, *path: str) -> None:
        """Write data to an attribute file."""

        try:
            with self.attr_path(*path).open(
                "w", encoding=DEFAULT_ENCODING
            ) as f:
                f.write(data)
        except PermissionError as exc:
            self.logger.exception("Couldn't write attribute:", exc_info=exc)

    def write_bool(self, value: bool, *path: str) -> None:
        """Write a boolean attribute."""
        self.write("1" if value else "0", *path)

    def write_int(self, value: int, *path: str) -> None:
        """Write an integer attribute."""
        self.write(str(value), *path)

    async def read_bool(self, *path: str) -> bool:
        """Attempt to read a boolean attribute."""

        return await self.aread(*path) == "1"

    async def read_int(self, *path: str) -> int:
        """Attempt to read an integer attribute."""

        return int(await self.aread(*path))

    @classmethod
    def instances(
        cls: Type[T],
        logger: LoggerType,
        *path: str,
        kind: Iterable[str] = None,
        attrs: Iterable[str] = None,
    ) -> Iterator[T]:
        """Iterate over instances found at some path."""

        candidate = SYS.joinpath(*cls.sys_path, *path)
        if candidate.is_dir():
            for item in candidate.iterdir():
                if item.is_dir():
                    inst = cls(logger, item)

                    # Check that the 'type' matches.
                    do_yield = (
                        True
                        if kind is None
                        else read_str(item.joinpath("type")).strip() in kind
                    )

                    # Check that desired attributes are present.
                    if do_yield and attrs:
                        for attr in attrs:
                            do_yield &= inst.has_attr(attr)

                    if do_yield:
                        yield inst


class SysClass(SysInstance):
    """A class for Linux devices under /sys/class."""

    sys_path = ["class"]
