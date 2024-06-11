"""
A module implementing a driver for an Owon bench power supply.
"""

# third-party
from runtimepy.net.arbiter.tcp import TcpConnectionFactory

# internal
from homestead.cots.scpi import ScpiConnection


class OwonConnection(ScpiConnection):
    """A simple Owon PSU driver class."""

    async def async_init(self) -> bool:
        """Initialize this instance."""

        result = await super().async_init()

        if result:
            await self.send_command("APP:VOLT", log=True, query=True)

        return result


class OwonConn(TcpConnectionFactory[OwonConnection]):
    """A connection factory for Owon devices."""

    kind = OwonConnection
