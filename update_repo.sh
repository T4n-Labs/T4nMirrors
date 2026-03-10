#!/bin/bash

set -e

echo "Updating XBPS repo..."

cd x86_64

rm -f repodata*

xbps-rindex -a *.xbps

echo "Repo updated"