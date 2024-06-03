# shellcheck source=../sh/common.sh
. "$HOMESTEAD/sh/common.sh"
. "$CWD/setme.sh"

APP_SRC=$CWD/apps/$APP.py
test "$APP_SRC"

CIRCUITPY=/mnt/CIRCUITPY
test "$CIRCUITPY"
