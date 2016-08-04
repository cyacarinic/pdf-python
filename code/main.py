import os
import sys
from falcon import API
from endpoints.routes import add_routes

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(BASE_DIR, 'endpoints'))

application = API()
add_routes(application)
