#!/bin/bash

set -e

PID=$(pgrep wvkbd)

if [ -n "$PID" ]; then
	# one opens it, one closes it
	# kill -SIGUSR1 "$PID"
	# kill -SIGUSR2 "$PID"
	kill -SIGRTMIN "$PID"
fi
