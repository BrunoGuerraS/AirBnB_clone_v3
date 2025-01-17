#!/usr/bin/python3
''' Start an  API'''
from flask import Flask, jsonify
from os import getenv
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardonw(self):
    '''To close storage '''
    return storage.close()


@app.errorhandler(404)
def page_not_found(e):
    '''Handler for 404 errors'''
    error = {"error": "Not found"}
    return (jsonify(error), 404)


if __name__ == '__main__':
    host = getenv("HBNB_API_HOST") if getenv("HBNB_API_HOST") else "0.0.0.0"
    port = getenv("HBNB_API_PORT") if getenv("HBNB_API_PORT") else 5000
    app.run(host=host, port=port, threaded=True)
