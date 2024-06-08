"""
A module implementing circuit-python related interfaces.
"""

# third-party
from runtimepy.net.arbiter.info import AppInfo
from vcorelib.asyncio.cli import run_shell

# internal
from homestead.serial import select_serial_port


async def reboot(app: AppInfo) -> int:
    """Use tio to reboot a circuit python device via serial REPL."""

    print(app)

    port = select_serial_port()
    print(port)

    # Simple reboot-to-bootloader program.
    program = "import microcontroller;"
    program += (
        "microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER);"
    )
    program += "microcontroller.reset();"
    shell = f'printf "\\r\\n%s\\r\\n" "{program}" | tio -r "{port}"'

    print(await run_shell(app.logger, shell))

    return 0
