# personal-web

[![Create Deployment](https://github.com/danlliu/personal-web/actions/workflows/deploy.yml/badge.svg)](https://github.com/danlliu/personal-web/actions/workflows/deploy.yml)
[![pages-build-deployment](https://github.com/danlliu/personal-web/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/danlliu/personal-web/actions/workflows/pages/pages-build-deployment)

My personal website.

## About This Project

This is my personal website! I've designed this with the mindset of a static website. The "backend" relies on a simple Python script ([src/render_templates.py](src/render_templates.py)) to render Jinja templates (located in the [templates/](templates) directory). Styling is taken care of by the Foundation front-end framework, as well as LESS files (located in [src/less/](src/less)). The Python script and Less compilation is wrapped into a deploy script ([deploy.sh](.ci/deploy.sh)) which is automatically run by GitHub actions on each push ([deploy.yml](.github/workflows/deploy.yml), special thanks to [@developStorm](https://github.com/developStorm) for the help!).

## How to Customize

If you'd like to create your website with a similar design, feel free to fork this repository. The main changes will be in [src/data](src/data), where the rendering script gets its information about the website contents.
