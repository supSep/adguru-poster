from flask import Flask
from flask.ext.restful import Api

from endpoints import ping, post
from endpoints.post import vancouver


app = Flask(__name__)
api = Api(app)


api.add_resource(post.vancouver.vancouver, '/vancouver/post/')  # <string:todo_id>')
api.add_resource(ping.ping, '/ping')  # <string:todo_id>')

if __name__ == '__main__':
    app.run(
        port=int("5000"),
        debug=True) #app.run(debug=True)