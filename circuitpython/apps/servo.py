from analogio import AnalogIn
from board import A0, GP2
from pwmio import PWMOut

POT = AnalogIn(A0)

# ADC values are 16-bit.
ANALOG_MAX = 2**16

# PWM duty-cycle resolution is also 16-bit.
DUTY_CYCLE_MAX = ANALOG_MAX

# 1 ms pulse minimum (5% of 20 ms / 50 Hz).
SERVO_DUTY_CYCLE_MIN = int(0.05 * DUTY_CYCLE_MAX)


def to_servo_duty_cycle(ratio: float) -> int:
    """Get a PWM duty-cycle value for a servo motor."""
    return SERVO_DUTY_CYCLE_MIN + int(0.05 * ratio * DUTY_CYCLE_MAX)


def pot_value() -> float:
    """Get the potentiometer value."""
    return POT.value / ANALOG_MAX


SERVO = PWMOut(GP2, frequency=50, duty_cycle=to_servo_duty_cycle(pot_value()))


print("Starting.")
while True:
    SERVO.duty_cycle = to_servo_duty_cycle(pot_value())
