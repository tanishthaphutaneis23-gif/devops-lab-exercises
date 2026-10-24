#!/usr/bin/env sh
set -eu
printf '%s\n' 'Hello, World from Jenkins!'
printf 'Build workspace: %s\n' "${WORKSPACE:-not-set}"
