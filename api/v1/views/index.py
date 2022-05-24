#!/usr/bin/python3
'''Creating flask '''
from api.v1.views import app_views
from flask import jsonify
import models
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def f_status_views():
    '''Method return a json format status'''
    data = {"status": "OK"}
    return (jsonify(data))


@app_views.route('/stats')
def retrieves_numbers():
    '''Endpoint that retrieves the number of each objects by type'''
    objs = {"amenities": models.storage.count(Amenity),
            "cities": models.storage.count(City),
            "places": models.storage.count(Place),
            "reviews": models.storage.count(Review),
            "states": models.storage.count(State),
            "users": models.storage.count(User)}
    return (jsonify(objs))
