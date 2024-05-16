#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
# shellcheck source=common.sh
. "$HOMESTEAD/pi5/common.sh"

safe_pushd "$HOMESTEAD"

mk rh

safe_popd
