#!/bin/sh

set -x

# Begin build process

cp -r src build

[ -d "src/less" ] && for f in src/less/*.less; do lessc $f > build/css/$(basename $f .less).css; done || true

python build/render_templates.py

# End build process
