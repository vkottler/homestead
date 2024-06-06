# shellcheck source=../sh/common.sh
. "$HOMESTEAD/sh/common.sh"
. "$CWD/setme.sh"

APP_SRC=$CWD/apps/$APP.py
test "$APP_SRC"

EMPTY="$CWD/apps/empty.py"
test "$EMPTY"

CIRCUITPY=/mnt/CIRCUITPY
test "$CIRCUITPY"

update_code() {
	set -x
	cp "$1" $CIRCUITPY/code.py
	set +x
}

update_repl() {
	set -x
	cp "$1" $CIRCUITPY/repl.py
	set +x
}
