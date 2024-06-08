"""
A module container for utilities.
"""

# pylint: disable=import-error

# embedded
import wifi  # type: ignore


def wifi_mac_addr() -> str:
    """Get this device's MAC address."""
    return ":".join([f"{i:x}" for i in wifi.radio.mac_address])
