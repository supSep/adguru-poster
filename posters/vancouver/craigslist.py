__author__ = 'sepehrtaheri'

from flask.ext.rq import job

#@job
def post(args):
    return args['category']