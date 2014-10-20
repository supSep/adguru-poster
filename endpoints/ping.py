import time

from flask import request, jsonify, make_response
from flask.ext.restful import Resource


class ping(Resource):
    def get(self):
        content = {"time": time.strftime("%b %d %Y %H:%M:%S", time.localtime()),
                   "response_code": 200,
                   "url": request.url,
                   "request_method": request.method,
                   "secure": request.is_secure}
        response = make_response(jsonify(content))
        response.headers['content-type'] = 'application/json'
        response.status_code = 200
        return response

    def post(self):
        return ping.get(self)