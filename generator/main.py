import os
import sys
from falcon import API
from api.routes import add_routes

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'api'))

application = API()

add_routes(application)

