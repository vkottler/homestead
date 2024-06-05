# pylint: disable=import-error
import board  # type: ignore
from digitalio import DigitalInOut, Direction  # type: ignore

print(__name__ + " begin.")

relay1 = DigitalInOut(board.GP14)
relay1.direction = Direction.OUTPUT

relay2 = DigitalInOut(board.GP15)
relay2.direction = Direction.OUTPUT

print(__name__ + " end.")
