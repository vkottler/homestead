#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=../common.sh
. "$CWD/common.sh"

"$CIRCUP" install adafruit_wiznet5k adafruit_requests

export EXIT=0
