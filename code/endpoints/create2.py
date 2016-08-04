# -*- coding: utf-8 -*-

import falcon
import json
import os
from utiles import _CreatePDF_fromURL, _CreatePDF_fromHTML, _CreatePDF_fromTEXT

class DocumentCollectionResource2(object):

	def on_post(self, req, resp):
		isMockup = req.get_param('mockup') or None
		if (isMockup):
			if isMockup == 'url':
				# Mockup para generar archivos pdfs desde una url
				url = ['http://divstyle.info', 'http://rcp.pe']
				name = []
				for x in url:
					try:
						name.append(_CreatePDF_fromURL(x))
					except Exception, e:
						print e
						resp.status = falcon.HTTP_400
					response_json = {"Ok":"Solicitud completada con éxito, se crearon los archivos %s."% name}
					resp.body = json.dumps(response_json)
					resp.status = falcon.HTTP_200
			elif isMockup == 'html':
				# Mockup para generar archivos pdfs desde un html
				html = ['Templates/basic.html']
				name = []
				for x in html:
					try:
						name.append(_CreatePDF_fromHTML(x))
					except Exception, e:
						print e
						resp.status = falcon.HTTP_400
					response_json = {"Ok":"Solicitud completada con éxito, se crearon los archivos %s."% name}
					resp.body = json.dumps(response_json)
					resp.status = falcon.HTTP_200
			elif isMockup == 'text':
				# Mockup para generar archivos pdfs desde un text
				text = ['Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eaque excepturi pariatur cupiditate iusto, ad cum magnam explicabo eos doloribus laudantium, eveniet deserunt fugiat ipsa nemo vel esse. Ad, non, temporibus!']
				name = []
				for x in text:
					try:
						name.append(_CreatePDF_fromTEXT(x))
					except Exception, e:
						print e
						resp.status = falcon.HTTP_400
					response_json = {"Ok":"Solicitud completada con éxito, se crearon los archivos %s."% name}
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
documentos2 = DocumentCollectionResource2()

# ruteado de la api
# wsgi_app.add_route('/api/v0.2/documents/pdfs', documentos2)
