#!/bin/bash

HOMESTEAD=$(git rev-parse --show-toplevel)
# shellcheck source=common.sh
. "$HOMESTEAD/pi5/common.sh"

RULES=$HOMESTEAD/pi5/99-backlight.rules

# Copy rules.
sudo cp "$RULES" /etc/udev/rules.d/

# Reload daemon (doesn't seem to be enough, probably because we would need to
# trigger some kind event).
sudo udevadm control --reload-rules
echo "Must reboot now."
