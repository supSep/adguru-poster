from flask import Flask
from flask.ext.restful import Api
from flask.ext.rq import RQ

from endpoints import ping, post
from endpoints.post import vancouver


app = Flask(__name__)
api = Api(app)
RQ(app)

# app.config['RQ_DEFAULT_HOST'] = 'somewhere.com'
# app.config['RQ_DEFAULT_PORT'] = 6479
# app.config['RQ_DEFAULT_PASSWORD'] = 'password'
# app.config['RQ_DEFAULT_DB'] = 1

api.add_resource(post.vancouver.vancouver, '/vancouver/post/')  # <string:todo_id>')
api.add_resource(ping.ping, '/ping')  # <string:todo_id>')

if __name__ == '__main__':
    app.run(
        port=int("5000"),
        debug=True) #app.run(debug=True)