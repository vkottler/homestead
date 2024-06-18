"""
A module implementing a Teledyne electronic load SCPI driver.
"""

# third-party
from runtimepy.net.arbiter.info import AppInfo
from runtimepy.net.arbiter.tcp import TcpConnectionFactory

# internal
from homestead.cots.scpi import ScpiConnection


class TeledyneConnection(ScpiConnection):
    """A simple Teledyne electronic load driver class."""

    async def async_init(self) -> bool:
        """Initialize this instance."""

        result = await super().async_init()

        if result:
            await self.send_command("*ESE", log=True, query=True)
            await self.send_command("*ESR", log=True, query=True)

        return result


async def test(app: AppInfo) -> int:
    """Run a simple test involving a Teledyne bench tool."""

    eload = app.single(kind=TeledyneConnection)

    # can do things with eload
    await eload.send_command("*IDN", log=True, query=True)

    return 0


class TeledyneConn(TcpConnectionFactory[TeledyneConnection]):
    """A connection factory for Teledyne devices."""

    kind = TeledyneConnection
