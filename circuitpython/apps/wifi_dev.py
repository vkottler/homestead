"""A sample circuit python program."""

# pylint: disable=import-error

# built-in
import ipaddress
import os
import time

# embedded
import socketpool  # type: ignore
import wifi  # type: ignore


def try_wifi() -> bool:
    """Attempt to connect to wifi."""

    ssid = os.getenv("CIRCUITPY_WIFI_SSID")
    passwd = os.getenv("CIRCUITPY_WIFI_PASSWORD")

    if ssid and passwd:
        print(f"Connecting to '{ssid}' ...")
        wifi.radio.connect(ssid, passwd)

    if wifi.radio.connected:
        print(f"Connected ({wifi.radio.ipv4_address}).")

    return wifi.radio.connected  # type: ignore


UDP = None
MTU = 1024


def udp_app(socket: socketpool.Socket) -> None:
    """A simple UDP application."""

    global UDP  # pylint: disable=global-statement
    UDP = socket

    input_buf = bytearray(MTU)

    iteration = 0

    while True:
        try:
            count, (host, port) = socket.recvfrom_into(input_buf)
            print(f"Got {count} bytes from {host}:{port}.")
            print(input_buf[:count])
        except OSError:
            pass

        socket.send(f"Hello, world! ({iteration})")

        time.sleep(1.0)

        iteration += 1


TLM_PORT = 7001


def udp_app_dest(dest_str: str, port: int = TLM_PORT) -> None:
    """Attempt to connect a UDP socket to the destination."""

    dest = ipaddress.IPv4Address(dest_str)

    if wifi.radio.ping(ip=dest) is not None:
        # Create and connect socket.
        pool = socketpool.SocketPool(wifi.radio)
        udp = pool.socket(type=pool.SOCK_DGRAM)
        udp.setblocking(False)
        udp.connect((dest_str, port))
        udp_app(udp)


def wifi_app() -> None:
    """A simple WiFi application."""

    if try_wifi():
        # amber-desktop, how would we DNS (mDNS)?
        udp_app_dest("192.168.8.248")


wifi_app()
