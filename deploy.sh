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

cd build

git init
git add -A
git branch -m main
git commit -m "Deploy to GitHub Pages"

git push -f git@github.com:danlliu/personal-web.git main:deploy

cd -
