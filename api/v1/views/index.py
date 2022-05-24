#!/usr/bin/python3
'''Creating flask '''
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status_views():
    '''Method return a json format status'''
    data = {"status": "OK"}
    return (jsonify(data))
