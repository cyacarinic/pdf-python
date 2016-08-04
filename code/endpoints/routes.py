import create, create2, create3, create4


def add_routes(app):
    app.add_route('/api/v0.1/documents/pdfs', create.DocumentCollectionResource())
    app.add_route('/api/v0.2/documents/pdfs', create2.DocumentCollectionResource2())
    app.add_route('/api/v0.3/documents/pdfs', create3.DocumentCollectionResource3())
    app.add_route('/api/v0.4/documents/pdfs', create4.DocumentCollectionResource4())
    