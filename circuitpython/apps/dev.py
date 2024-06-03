"""
A sample Circuit Python program.
"""

# pylint: disable=import-error
import time

import board  # type: ignore
from digitalio import DigitalInOut, Direction  # type: ignore

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT


def main() -> None:
    """Application entry."""

    iteration = 0

    while True:
        led.value = not led.value
        time.sleep(0.1)
        iteration += 1
        print(f"iteration: {iteration}")


if __name__ == "__main__":
    main()
