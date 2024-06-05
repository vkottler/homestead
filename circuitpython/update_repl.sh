#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

set -x
cp "$CWD/apps/repl.py" $CIRCUITPY/repl.py
set +x

EXIT=0
