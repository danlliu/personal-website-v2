#!/bin/sh

set -x

# Begin build process

rm -rf build/
mkdir -p build/
mkdir -p build/js
mkdir -p build/css

cp src/*.html build/
cp src/js/* build/js

# End build process
