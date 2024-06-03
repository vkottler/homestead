#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

# Reboot RP2040 bootloader to application.
picotool reboot -a

EXIT=0
