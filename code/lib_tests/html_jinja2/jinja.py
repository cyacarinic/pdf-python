# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(THIS_DIR, "templates/")

def print_html_doc():
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
                         trim_blocks=True)
    template = env.get_template('my_template.html')
    return template.render()

if __name__ == '__main__':
    print_html_doc()
