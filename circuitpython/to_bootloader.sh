#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

# PORT="$(get_serial_port)"

# Simple reboot-to-bootloader program.
# PROGRAM="import microcontroller;"
# PROGRAM+="microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER);"
# PROGRAM+="microcontroller.reset();"

# printf "\r\n%s\r\n" "$PROGRAM" | tio -r "$PORT"

run_mk rh-reboot

EXIT=0
