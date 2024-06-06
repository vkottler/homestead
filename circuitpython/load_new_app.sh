#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/circuitpython"
# shellcheck source=common.sh
. "$CWD/common.sh"

update_code "$APP_SRC"

EXIT=0
