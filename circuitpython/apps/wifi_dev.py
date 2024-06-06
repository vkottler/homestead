# pylint: disable=import-error

# built-in
import os

# embedded
import wifi


def mac_addr() -> str:
    """Get this device's MAC address."""
    return ":".join([f"{i:x}" for i in wifi.radio.mac_address])


def try_wifi() -> None:
    """Attempt to connect to wifi."""

    ssid = os.getenv("CIRCUITPY_WIFI_SSID")
    passwd = os.getenv("CIRCUITPY_WIFI_PASSWORD")

    if ssid and passwd:
        print(f"Connecting to '{ssid}' ...")
        wifi.radio.connect(ssid, passwd)
        print(f"Connected ({wifi.radio.ipv4_address}).")


try_wifi()
