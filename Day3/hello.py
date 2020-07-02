#!/usr/bin/python3
import flask
import os

app = flask.Flask(__name__)

@app.route('/<string:msg>', methods=['GET'])
def home(msg):
    s = os.environ.get('MESSAGE')
    return s + " " + msg 

app.run(host='0.0.0.0', port=80)
