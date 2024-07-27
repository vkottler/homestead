#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=../common.sh
. "$CWD/common.sh"

"$CIRCUP" list

export EXIT=0
