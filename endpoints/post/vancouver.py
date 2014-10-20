from flask import request, jsonify, make_response
from flask.ext.restful import Resource, marshal_with, fields, reqparse
import re
from flask.ext.rq import get_queue
import time
from werkzeug.routing import ValidationError
from posters.vancouver import main


def email(email_str):
    """ return True if email_str is a valid email """
    if re.match(r"[^@]+@[^@]+\.[^@]+", email_str):
        return True
    else:
        raise ValidationError("{} is not a valid email")


def phone(phone_str):
    """ return True if email_str is a valid email """
    if re.match(r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$", phone_str):
        return True
    else:
        raise ValidationError("{} is not a valid phone number")


post_parser = reqparse.RequestParser()

post_parser.add_argument(
    'id',type=str, location='json', dest='id'
    , required=True, help='The user\'s username id')

post_parser.add_argument(
'email', dest='email',
    type=email, location='json',

)
post_parser.add_argument(
    'category', dest='category',
    type=str, location='json',
    required=True, help='The user\'s category',
)
post_parser.add_argument(
    'location', dest='location',
    type=str, location='json',
    required=True, help='The user\'s location',
)
post_parser.add_argument(
    'phone', dest='phone',
    type=phone, location='json',
    required=True, help='The user\'s phone',
)
post_parser.add_argument(
    'description', dest='description',
    type=str, location='json',
    required=True, help='The user\'s description',
)
post_parser.add_argument(
    'price', dest='price',
    type=float, location='json',
    required=True, help='The user\'s price',
)
post_parser.add_argument(
    'title', dest='title',
    type=str, location='json',
    required=True, help='The user\'s Title',
)

user_fields = {
    'id': fields.String,
    'category': fields.String,
    'location': fields.String,
    'title' : fields.String,
    'email': fields.String,
    'phone': fields.String,
    'description': fields.String,
    'price': fields.String
}


class vancouver(Resource):
    @marshal_with(user_fields)
    def post(self):
        args = post_parser.parse_args()
        job = main.post(args)

        print("before sleep", job)

        time.sleep(1)

        print("after sleep", job)
        print("result", job)

        return dict(title=job)

    def get(self):
        content = {"time": 123,
                   "response_code": 200,
                   "url": request.url,
                   "request_method": request.method,
                   "secure": request.is_secure}
        response = make_response(jsonify(content))
        response.headers['content-type'] = 'application/json'
        response.status_code = 200
        return response