# Link workspace.
if [ ! -L "$HOMESTEAD/workspace" ]; then
	ln -s ~/src/project-81/workspace "$HOMESTEAD/workspace"
fi

# Load workspace scripts.
REPO=$HOMESTEAD/workspace
# shellcheck source=../workspace/scripts/common.sh
. "$REPO/scripts/common.sh"
