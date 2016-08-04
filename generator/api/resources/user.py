import json
from falcon import HTTPError


class UsersCollectionResource:

    def on_get(self, req, resp):
    	resp.body = json.dumps({"demo": "get"}, indent=4)

    def on_post(self, req, resp):
        resp.body = json.dumps({"demo": "post"}, indent=4)
