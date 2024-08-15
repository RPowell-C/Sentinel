from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import logging

app = Flask(__name__)
cors = CORS(app)
api = Api(app)
log = logging.getLogger('werkzeung').disabled = True
app.logger.setLevel(logging.ERROR)
app.config['CORS_HEADERS'] = 'Content-Type'

class HelloWorld(Resource):
    def get(self):
        global global_username
        global global_message
        return {'Username': global_username, 'Message': global_message}

api.add_resource(HelloWorld, '/')

def update_username(username):
    global global_username
    global_username = username
def update_message(message):
    global global_message
    global_message = message


def shitfuck():
    app.run()
