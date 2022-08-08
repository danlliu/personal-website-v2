#!/bin/sh

set -x

# Begin build process

cp -r src build

[ -d "build/css" ] || mkdir -p build/css
[ -d "src/less" ] && for f in src/less/*.less; do lessc $f > build/css/$(basename $f .less).css; done || true

python3 build/fetch_icon_colors.py
python3 build/render_templates.py

# End build process
