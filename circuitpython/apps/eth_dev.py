"""A sample circuit python program."""

# built-in
import time

# embedded
# pylint: disable=import-error
import adafruit_connection_manager  # type: ignore
import adafruit_requests  # type: ignore
from adafruit_wiznet5k.adafruit_wiznet5k import WIZNET5K  # type: ignore
import board  # type: ignore
import busio  # type: ignore
import digitalio  # type: ignore

print("Wiznet5k WebClient Test")

# Reset W5x00 first
ethernetRst = digitalio.DigitalInOut(
    board.W5500_RST  # pylint: disable=no-member
)

ethernetRst.direction = digitalio.Direction.OUTPUT
ethernetRst.value = False
time.sleep(1)
ethernetRst.value = True

# Initialize ethernet interface with DHCP
eth = WIZNET5K(
    busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO),
    digitalio.DigitalInOut(board.W5500_CS),  # pylint: disable=no-member
    is_dhcp=True,
    debug=False,
)
print("Chip Version:", eth.chip)
print("MAC Address:", [hex(i) for i in eth.mac_address])
print("My IP address is:", eth.pretty_ip(eth.ip_address))
print(
    "IP lookup adafruit.com: "
    f"{eth.pretty_ip(eth.get_host_by_name('adafruit.com'))}"
)

# Initialize a requests session
requests = adafruit_requests.Session(
    adafruit_connection_manager.get_radio_socketpool(eth),
    adafruit_connection_manager.get_radio_ssl_context(eth),
)

# eth._debug = True
TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"
print("Fetching text from", TEXT_URL)
r = requests.get(TEXT_URL)
print("-" * 40)
print(r.text)
print("-" * 40)
r.close()

print()
JSON_URL = "http://api.coindesk.com/v1/bpi/currentprice/USD.json"
print("Fetching json from", JSON_URL)
r = requests.get(JSON_URL)
print("-" * 40)
print(r.json())
print("-" * 40)
r.close()

print("Done!")
