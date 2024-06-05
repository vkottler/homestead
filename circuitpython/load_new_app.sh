#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

set -x
cp "$APP_SRC" $CIRCUITPY/code.py
set +x

EXIT=0
