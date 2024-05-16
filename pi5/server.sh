#!/bin/bash

REPO=$(git rev-parse --show-toplevel)
# shellcheck source=common.sh
. "$REPO/pi5/common.sh"

pushd "$REPO" >/dev/null || exit 1

mk rh

popd >/dev/null || exit 1
