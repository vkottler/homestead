get_serial_port() {
	# Eventually this should be more sophisticated.
	result=$(tio -L | head -n 1)
	echo "Serial port selected: '$result'." >&2
	echo "$result"
}

run_mk() {
	mk -C "$HOMESTEAD" "$@"
}

CIRCUP="$HOMESTEAD/venv/bin/circup"
if ! [ -f "$CIRCUP" ]; then
	run_mk venv
fi
