#!/bin/bash

set -e

PID=TODO

# one opens it, one closes it
kill -SIGUSR1 $PID
kill -SIGUSR2 $PID
