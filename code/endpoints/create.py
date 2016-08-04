# -*- coding: utf-8 -*-

import falcon
import json
from settings import _OFFSET_GET, _LIMIT_GET
from utiles import _get_campo, _item_respuesta
from create2 import documentos2
from create3 import documentos3
from create4 import documentos4

class DocumentCollectionResource(object):

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


	def on_post(self, req, resp):
		isMockup = req.get_param('mockup') or None
		if(isMockup):
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
				result_json_list.append(_item_respuesta(item))

			resp.status = falcon.HTTP_202
		else:
			# creacion de pdf
			# Choclon de código
			result_json_list = {"Error":
				"Método POST no disponible. Probar Mockup."}
			resp.status = falcon.HTTP_404

		resp.body = json.dumps(result_json_list, indent=4,
		 	encoding='utf-8', sort_keys=True)

# las instancias falcon.API son apps WSGI
wsgi_app = falcon.API()

# instancias de las clases
documentos = DocumentCollectionResource()

# ruteado de la api
wsgi_app.add_route('/api/v0.1/documents/pdfs', documentos)
wsgi_app.add_route('/api/v0.2/documents/pdfs', documentos2)
wsgi_app.add_route('/api/v0.3/documents/pdfs', documentos3)
wsgi_app.add_route('/api/v0.4/documents/pdfs', documentos4)
# wsgi_app.add_route('/api/v0.1/documents/pdfs/{id}', documentoSingle)
