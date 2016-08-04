# -*- coding: utf-8 -*-

import pdfkit
import time
import	os
from datetime import datetime as dt
from settings import _BASE_DIR, _PATH_URL, _PATH_HTML, _PATH_TEXT
from settings import _PATH_TEMPLATE, _FILE_TYPES
from Templates.html_jinja2.jinja import print_html_doc as template_render

# ==============================================================================

_FILE_TYPE = '.pdf'

def _CreatePDF_fromURL(url):
	name = os.path.basename(url)+_FILE_TYPE
	pdfkit.from_url(html, "pdfs/from_url/%s" % (name))
	return name


def _CreatePDF_fromHTML(html):
	name = os.path.basename(html)+_FILE_TYPE
	pdfkit.from_file(html, "pdfs/from_html/%s" % (name))
	return name

def _CreatePDF_fromTEXT(text):
	name = "Test"+_FILE_TYPE
	pdfkit.from_string(text, "pdfs/from_text/%s" % (name))
	return name

# ==============================================================================

def _create_document(resource, method, type_document):
	print "RECURSO ----> %s" %str(resource)
	print "METODO ----> %s" %str(method)


	if method == "url":
		path_document = _PATH_URL
	elif method == "html":
		path_document = _PATH_HTML
	elif method == "template":
		resource = template_render(resource)
		path_document = _PATH_TEMPLATE
	else:
		# method == "text"
		path_document = _PATH_TEXT

	# Verifica la existencia de la carpeta de pdfs
	if not os.path.isdir(path_document):
		try:
			os.makedirs(path_document)
		except Exception, e:
			respuesta = { "Error":str(e) }
	if method == "template":
		file_name = "template"
	elif method == "text":
		file_name = "text"
	else:
		file_name = "%s" %os.path.basename(resource)
	file_route = os.path.join(path_document, file_name+type_document)
	# Verifica si ya existe un archivo con el mismo nombre
	if os.path.exists(file_route):
		file_name = "%s-%s" %(file_name, time.strftime("%Y%m%d-%H%M%S"))
		file_route = os.path.join(path_document, file_name+type_document)

	try:
		if method == "url" :
			pdfkit.from_url(str(resource), file_route)
		elif method == "html":
			pdfkit.from_file(str(resource), file_route)
		elif method == "template":
			pdfkit.from_string(resource, file_route)
		else:
			# method == "text" or method == "template"
			pdfkit.from_string(str(resource), file_route)

		respuesta = "%s%s" %(file_name, type_document)
	except Exception, e:
		respuesta = { "Error":str(e) }
	return respuesta

# ==============================================================================

def _get_campo(diccionario, campo, default):
	if diccionario.has_key(campo):
		return diccionario.pop(campo)
	else:
		return default

def _item_respuesta(diccionario_item):
	doc_tipo = diccionario_item.pop("type", None)
	doc_contenido = diccionario_item.pop("content", None)
	if type(doc_contenido) != type([""]):
		doc_contenido = [doc_contenido]
	doc_paginas = len(doc_contenido)
	doc_accion = _get_campo(diccionario_item, "action", "create")
	doc_fecha = _get_campo(diccionario_item, "date", dt.today())
	doc_titulo = _get_campo(diccionario_item, "title", "DOC000001")
	doc_autor = _get_campo(diccionario_item, "autor", "SYSTEM")

	item_result = {
		"tipo":doc_tipo
	}
	json_pages = {}
	for pagina in range(doc_paginas):
		json_pages.update({
			"pagina_%i" %(pagina+1) : doc_contenido[pagina]
		})
	item_result.update({"documento":json_pages})
	item_result.update({"numero_paginas":doc_paginas})
	item_result.update({"accion":doc_accion})
	item_result.update({"fecha_creacion":str(doc_fecha)})
	item_result.update({"titulo_documento":doc_titulo})
	item_result.update({"autor_documento":doc_autor})

	return item_result

# ==============================================================================

def _item_create(diccionario_item):
	doc_tipo = diccionario_item.pop("type", None)
	doc_contenido = diccionario_item.pop("content", None)
	doc_metodo = diccionario_item.pop("method", None)
	if type(doc_contenido) != type([""]):
		doc_contenido = [doc_contenido]
	doc_paginas = len(doc_contenido)
	doc_accion = _get_campo(diccionario_item, "action", "create")
	doc_fecha = _get_campo(diccionario_item, "date", dt.today())
	doc_titulo = _get_campo(diccionario_item, "title", "DOC000001")
	doc_autor = _get_campo(diccionario_item, "autor", "SYSTEM")

	item_result = {
		"tipo":doc_tipo
	}
	json_pages = {}
	for pagina in range(doc_paginas):
		json_pages.update({
			"pagina_%i" %(pagina+1) : _create_document(doc_contenido[pagina],
							doc_metodo, ".%s" %str(doc_tipo))
		})
	item_result.update({"documento":json_pages})
	item_result.update({"numero_paginas":doc_paginas})
	item_result.update({"accion":doc_accion})
	item_result.update({"fecha_creacion":str(doc_fecha)})
	item_result.update({"titulo_documento":doc_titulo})
	item_result.update({"autor_documento":doc_autor})

	return item_result
