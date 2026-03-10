#!/bin/bash

echo "Updating XBPS repository..."

rm -f repodata*

xbps-rindex -a *.xbps

echo "Repository updated."

# scan paket
# generate repodata
# xbps bisa membaca repo