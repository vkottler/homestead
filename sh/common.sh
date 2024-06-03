# shellcheck source=functions.sh
. "$HOMESTEAD/sh/functions.sh"

# Link workspace.
if [ ! -L "$HOMESTEAD/workspace" ]; then
	ln -s ~/src/project-81/workspace "$HOMESTEAD/workspace"
fi

# Load workspace scripts.
REPO=$HOMESTEAD/workspace
# shellcheck source=../workspace/scripts/common.sh
. "$REPO/scripts/common.sh"

# Must be set to 0 by application script.
EXIT=-1

if [ -d "$CWD" ]; then
	if [ -f "$CWD/functions.sh" ]; then
		. "$CWD/functions.sh"
	fi

	safe_pushd "$CWD"

	cleanup() {
		echo "Exit: $EXIT".
		safe_popd
	}

	trap cleanup EXIT
fi
