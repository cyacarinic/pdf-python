# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import os

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(THIS_DIR, "templates/")

def print_html_doc(dic_kwargs):
    nombre = dic_kwargs["nombre"] if "nombre" in dic_kwargs else None
    apellido = dic_kwargs["apellido"] if "apellido" in dic_kwargs else None
    texto = dic_kwargs["texto"] if "texto" in dic_kwargs else None

    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR),
                         trim_blocks=True)
    template = env.get_template('my_template.html')
    rendereado = template.render(Nombre=nombre, Apellido=apellido,
        Texto=texto)
    return rendereado

if __name__ == '__main__':
    print_html_doc()
