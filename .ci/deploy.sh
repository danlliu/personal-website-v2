#!/bin/sh

set -x

# Begin build process

rm -rf build/
mkdir -p build/
mkdir -p build/js
mkdir -p build/css

cp -R src/ build/
[ -d "src/less" ] && for f in src/less/*.less; do lessc $f > build/css/$(basename $f .less).css; done || true

python3 build/render_templates.py

# End build process
