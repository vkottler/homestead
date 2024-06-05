"""
A sample Circuit Python program.
"""

# pylint: disable=import-error
import time

import board  # type: ignore
from digitalio import DigitalInOut, Direction  # type: ignore

led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

# relay1 = DigitalInOut(board.GP14)
# relay1.direction = Direction.OUTPUT

# relay2 = DigitalInOut(board.GP15)
# relay2.direction = Direction.OUTPUT


def main() -> None:
    """Application entry."""

    iteration = 0

    for _ in range(3):
        led.value = not led.value
        time.sleep(0.1)
        iteration += 1
        print(f"iteration: {iteration}")


if __name__ == "__main__":
    main()
