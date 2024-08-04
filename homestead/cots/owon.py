"""
A module implementing a driver for an Owon bench power supply.
"""

# third-party
from runtimepy.net.arbiter.info import AppInfo
from runtimepy.net.arbiter.tcp import TcpConnectionFactory

# internal
from homestead.cots.scpi import ScpiConnection


class OwonConnection(ScpiConnection):
    """A simple Owon PSU driver class."""

    async def query_all_measured_voltage(self) -> list[float]:
        """Query all measured voltage channels."""

        return list(
            map(
                float,
                (await self.send_command("MEAS:VOLT:ALL", query=True))
                .rstrip()
                .split(", "),
            )
        )

    async def query_measured_voltage(self) -> list[float]:
        """Query all measured current channels."""

        return list(
            map(
                float,
                (await self.send_command("MEAS:VOLT", query=True))
                .rstrip()
                .split(", "),
            )
        )

    async def query_all_measured_current(self) -> list[float]:
        """Query all measured current channels."""

        return list(
            map(
                float,
                (await self.send_command("MEAS:CURR:ALL", query=True))
                .rstrip()
                .split(", "),
            )
        )

    async def query_measured_current(self) -> list[float]:
        """Query all measured current channels."""

        return list(
            map(
                float,
                (await self.send_command("MEAS:CURR", query=True))
                .rstrip()
                .split(", "),
            )
        )

    async def query_set_voltage(self) -> list[float]:
        """Query set voltage channels."""

        return list(
            map(
                float,
                (await self.send_command("APP:VOLT", query=True))
                .rstrip()
                .split(", "),
            )
        )

    async def async_init(self) -> bool:
        """Initialize this instance."""

        result = await super().async_init()

        #  if result:
        #    response = await self.send_command("APP:VOLT", query=True)

        return result


async def test(app: AppInfo) -> int:
    """Run a simple test involving an Owon power supply."""

    psu = app.single(kind=OwonConnection)
    for _ in range(5):
        print(await psu.query_set_voltage())
        print(await psu.query_all_measured_voltage())
        print(await psu.query_measured_voltage())
        print(await psu.query_all_measured_current())
        print(await psu.query_measured_current())

    # can do things with psu
    return 0


class OwonConn(TcpConnectionFactory[OwonConnection]):
    """A connection factory for Owon devices."""

    kind = OwonConnection
