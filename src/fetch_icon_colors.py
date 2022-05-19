
import json
from pathlib import Path
import re

import requests

SIMPLE_ICONS_JSON = 'https://cdn.jsdelivr.net/npm/simple-icons@6.20.0/_data/simple-icons.json'

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH / 'data'
TEMPLATE_PATH = ROOT_PATH / 'templates'


def match_icons(context):
    """
    Iterate through the context object, looking for an array called langs.
    """
    results = []
    
    if isinstance(context, dict):
        for key, value in context.items():
            if key == 'langs':
                results += value
            else:
                results += match_icons(value)
    elif isinstance(context, list):
        for item in context:
            results += match_icons(item)

    return results


if __name__ == '__main__':
    # Open DATA_PATH / icon-colors.json as JSON.
    with open(DATA_PATH / 'icon_colors.json', 'r') as f:
        data = f.read()
    colors = json.loads(data)

    all_icons = set()

    # Iterate through each file in DATA_PATH.
    for file in DATA_PATH.iterdir():
        # Read JSON contents of file.
        with open(file, 'r') as f:
            data = f.read()
        data = json.loads(data)

        if 'context' not in data:
            continue

        context = data['context']
        icons = match_icons(context)
        print(icons)
        for i in icons:
            all_icons.add(i)

    # Fetch all colors and titles.

    select_colors = {}
    select_titles = {}
    select_paths = {}

    for i in all_icons:
        select_colors[i] = colors[i]['hex']
        select_titles[i] = colors[i]['title']
        select_paths[i] = colors[i]['path']

    print(json.dumps(select_colors))
    print(json.dumps(select_titles))

    # Write to DATA_PATH / select_icon-colors.json.
    with open(DATA_PATH / 'select_icon_colors.json', 'w') as f:
        f.write(json.dumps(select_colors))

    # Write to DATA_PATH / select_icon-titles.json.
    with open(DATA_PATH / 'select_icon_titles.json', 'w') as f:
        f.write(json.dumps(select_titles))

    # Write to DATA_PATH / select_icon-svgs.json.
    with open(DATA_PATH / 'select_icon_paths.json', 'w') as f:
        f.write(json.dumps(select_paths))