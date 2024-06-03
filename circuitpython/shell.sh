#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

PORT="$(get_serial_port)"

tio "$PORT"

EXIT=0
