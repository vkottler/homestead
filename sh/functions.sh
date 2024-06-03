banner() {
	echo "================================================================"
}

banner_for_file() {
	banner
	echo "Contents of '$1' below."
	banner
	cat "$1"
	banner
}
