# -*- coding: utf-8 -*-

import falcon
import json
import os
from settings import _FILE_TYPES, _OFFSET_GET, _LIMIT_GET
from utiles import _item_create

class DocumentCollectionResource4(object):

	def on_post(self, req, resp):
		isMockup = req.get_param('mockup') or None
		if (isMockup):
			if (isMockup == "url" or isMockup == "html" or
			 	isMockup == "text" or isMockup == "template"):
				try:
					raw_request = req.stream.read()
					# tipo string
				except Exception as ex:
					raise falcon.HTTPError(falcon.HTTP_400,
						'Error', ex.message)
				try:
					doc_json = json.loads(raw_request,
						encoding='utf-8')
					# tipo dict (segun estandares tipo list)
				except ValueError:
					raise falcon.HTTPError(falcon.HTTP_400,
						'Formato erroneo JSON',
						'No se pudo decodificar. JSON erroneo.')

				if type(doc_json) != type([""]):
					doc_json = [doc_json]

				result_json_list = []
				for item in doc_json:
					# print "|----> ITEM"
					# print _item_create(item)
					result_json_list.append(_item_create(item))

				resp.body = json.dumps(result_json_list)
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
		if(isMockup):
			try:
				with open('responses.json') as data_file:
					data = json.load(data_file)
			except IOError:
				with open('responses.json','w') as data_file:
					data_file.write("[]")
				data = []
			# data = json.load(open('responses.json'))
			result_json = {
			    "metadata": {
			        "resultset": {
			            "count": len(data),
			            "offset": _OFFSET_GET,
			            "limit": _LIMIT_GET,
			        }
			    },
			    "results": data
			}
			resp.status = falcon.HTTP_200
		else:
			# creacion de pdf
			# Choclon de código
			result_json = {"Error":"Metodo GET no disponible. Probar Mockup."}
			resp.status = falcon.HTTP_404

		resp.body = json.dumps(result_json, indent=4,
		encoding='utf-8', sort_keys=True)

wsgi_app = falcon.API()

# instancias de las clases
documentos4 = DocumentCollectionResource4()

# ruteado de la api
# wsgi_app.add_route('/api/v0.4/documents/pdfs', documentos4)
