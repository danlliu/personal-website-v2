#!/bin/sh

set -x

# Begin build process

ls

mkdir build/

ls
ls build

cp -R src/ build/
[ -d "build/css" ] && mkdir -p build/css || true

ls
ls build

[ -d "src/less" ] && for f in src/less/*.less; do lessc $f > build/css/$(basename $f .less).css; done || true

ls
ls build

python build/render_templates.py

# End build process
