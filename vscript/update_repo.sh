#!/usr/bin/env bash

set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "Updating XBPS repository..."

cd "$REPO_ROOT/x86_64"

# hapus metadata lama
rm -rf *-repodata

# generate metadata repo
xbps-rindex -a *.xbps

echo "XBPS repository metadata updated."