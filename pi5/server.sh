#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
CWD="$HOMESTEAD/pi5"
# shellcheck source=common.sh
. "$CWD/common.sh"

safe_pushd "$HOMESTEAD"

mk rh

safe_popd
