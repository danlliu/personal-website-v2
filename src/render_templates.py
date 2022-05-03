#!/usr/bin/python3

import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH / 'data'
TEMPLATE_PATH = ROOT_PATH / 'templates'

env = Environment(
    loader=FileSystemLoader(TEMPLATE_PATH),
    autoescape=select_autoescape()
)

if __name__ == '__main__':
    # Iterate through each file in DATA_PATH.
    for file in DATA_PATH.iterdir():
        # Read JSON contents of file.
        with open(file, 'r') as f:
            data = f.read()
        data = json.loads(data)

        template = env.get_template(data['base_template'])
        print('Rendering template {}'.format(data['base_template']))
        rendered = template.render(**data['context'])
        with open(ROOT_PATH / data['path'], 'w') as f:
            f.write(rendered)
