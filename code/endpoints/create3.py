# -*- coding: utf-8 -*-

import falcon
import json
import os
from settings import _FILE_TYPES
from utiles import _create_document
from Templates.html_jinja2.jinja import print_html_doc as template_render

class DocumentCollectionResource3(object):

	def on_post(self, req, resp):
		isMockup = req.get_param('mockup') or None
		if (isMockup):
			if (isMockup == "url" or isMockup == "html" or
			 	isMockup == "text" or isMockup == "template"):
				# Mockup Genérico
				if isMockup == "url":
					resource = "http://divstyle.info"
				elif isMockup == "html":
					resource = "Templates/basic.html"
				elif isMockup == "text":
					resource = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. \
					Eaque excepturi pariatur cupiditate iusto, ad cum magnam explicabo eos \
					doloribus laudantium, eveniet deserunt fugiat ipsa nemo vel esse. Ad, \
					non, temporibus!"
				else:
					resource = template_render()
				responses = []
				for documento in range(2):
					responses.append(
						_create_document(resource, isMockup, _FILE_TYPES[0]))
				response_json = {
					"Responses":responses
				}
				resp.body = json.dumps(response_json)
				resp.status = falcon.HTTP_200
			else:
				# Si el valor del mockup no es el correcto
				response_json = {"Error":"Mockup disponible solo para url, html o text"}
				resp.body = json.dumps(response_json)
				resp.status = falcon.HTTP_200
		else:
			# Aca ira todo el codigo para crear el PDF sin mockup
			response_json = {"Error":"Método POST no disponible. Probar Mockup."}
			resp.status = falcon.HTTP_404
			resp.body = json.dumps(response_json, indent=4, encoding='utf-8', sort_keys=True)

	def on_get(self, req, resp):
		isMockup = req.get_param('mockup') or None
		if (isMockup):
			try:
				# El mockup listara el nombre de todos los archivos pdf generados
				lstFiles = []
				lstDir = os.walk("pdfs/")
				for root, dirs, files in lstDir:
					for fichero in files:
						(nombre, extension) = os.path.splitext(fichero)
						lstFiles.append(nombre+extension)
				resp.body = json.dumps(lstFiles)
				resp.status = falcon.HTTP_200
			except Exception, e:
				print e
				resp.status = falcon.HTTP_400
		else:
			response_json = {"Error":"Método GET no disponible. Probar Mockup."}
			resp.status = falcon.HTTP_404
			resp.body = json.dumps(response_json, indent=4, encoding='utf-8', sort_keys=True)

wsgi_app = falcon.API()

# instancias de las clases
documentos3 = DocumentCollectionResource3()

# ruteado de la api
# wsgi_app.add_route('/api/v0.3/documents/pdfs', documentos3)
