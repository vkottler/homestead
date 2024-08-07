"""
A module implementing an SCPI interface.
"""

# built-in
import asyncio

# third-party
from runtimepy.net.tcp import TcpConnection


class ScpiConnection(TcpConnection):
    """A simple SCPI connection class."""

    def init(self) -> None:
        """Initialize this instance."""

        self.command_lock = asyncio.Lock()
        self.message_queue: asyncio.Queue[str] = asyncio.Queue(maxsize=1)

    async def async_init(self) -> bool:
        """Initialize this instance."""

        return bool(await self.send_command("*IDN", log=True, query=True))

    async def process_text(self, data: str) -> bool:
        """Process a text frame."""

        for item in data.split("\r\n"):
            if item:
                await self.message_queue.put(item)

        return True

    async def process_binary(self, data: bytes) -> bool:
        """Process a binary frame."""
        return await self.process_text(data.decode())

    async def send_command(
        self,
        command: str,
        response: bool = True,
        log: bool = False,
        query: bool = False,
        timeout: float = 1.0,
    ) -> str:
        """Send a command."""

        result = ""

        if query:
            command += "?"

        async with self.command_lock:
            self.send_text(command + "\n")

            if response or query:
                try:
                    result = await asyncio.wait_for(
                        self.message_queue.get(), timeout
                    )
                    if log:
                        self.logger.info("(%s) %s", command, result.rstrip())
                except asyncio.TimeoutError:
                    pass

        return result
