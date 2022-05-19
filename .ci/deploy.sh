#!/bin/sh

set -x

# Begin build process

cp -r src build

[ -d "build/css" ] || mkdir -p build/css
[ -d "src/less" ] && for f in src/less/*.less; do lessc $f > build/css/$(basename $f .less).css; done || true

python build/fetch_icon_colors.py
python build/render_templates.py

# End build process
