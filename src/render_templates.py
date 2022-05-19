#!/usr/bin/python3

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape
import requests

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH / 'data'
TEMPLATE_PATH = ROOT_PATH / 'templates'

SIMPLE_ICONS_COLORS = DATA_PATH / 'select_icon_colors.json'
SIMPLE_ICONS_TITLES = DATA_PATH / 'select_icon_titles.json'
SIMPLE_ICONS_PATHS = DATA_PATH / 'select_icon_paths.json'

env = Environment(
    loader=FileSystemLoader(TEMPLATE_PATH),
    autoescape=select_autoescape()
)

if __name__ == '__main__':
    # Read SIMPLE_ICONS_COLORS JSON.
    with open(SIMPLE_ICONS_COLORS, 'r') as f:
        data = f.read()
    colors = json.loads(data)

    # Read SIMPLE_ICONS_TITLES JSON.
    with open(SIMPLE_ICONS_TITLES, 'r') as f:
        data = f.read()
    titles = json.loads(data)

    # Read SIMPLE_ICONS_SVGS JSON.
    with open(SIMPLE_ICONS_PATHS, 'r') as f:
        data = f.read()
    paths = json.loads(data)

    # Iterate through each file in DATA_PATH.
    for file in DATA_PATH.iterdir():
        # Read JSON contents of file.
        with open(file, 'r') as f:
            data = f.read()
        data = json.loads(data)
        if 'base_template' not in data:
            continue

        template = env.get_template(data['base_template'])
        print('Rendering template {}'.format(data['base_template']))

        context = data['context']

        context['colors'] = colors
        context['titles'] = titles
        context['paths'] = paths

        rendered = template.render(**context)
        with open(ROOT_PATH / data['path'], 'w') as f:
            f.write(rendered)
