import settings
from resources.user import UsersCollectionResource

def add_routes(app):
    app.add_route('/users', UsersCollectionResource())
