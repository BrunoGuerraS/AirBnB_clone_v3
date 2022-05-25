#!/usr/bin/python3
'''Script view for State objects that handles all default RESTFul API
actions '''
from flask import jsonify, abort, request
from models import storage
from models.state import State
from api.v1.views import app_views


@app_views.route('/states', methods=["GET"], strict_slashes=False)
def state_views():
    '''Retrieves all default actions in JSON format'''
    data = []
    for i in storage.all().values():
        data.append(i.to_dict())
    return (jsonify(data))


@app_views.route('states/<state_id>', methods=["GET"], strict_slashes=False)
def state_list(state_id):
    '''Retrieves ID '''
    data = storage.get(State, state_id)
    if data is None:
        abort(404)
    return (jsonify(data.to_dict()))


@app_views.route('/states/<state_id>', methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    '''Deletes '''
    data = storage.get(State, state_id)
    if data is None:
        abort(404)
    data.delete()
    storage.save()
    return jsonify({})


@app_views.route('/states', methods=["POST"], strict_slashes=False)
def post_state():
    '''Transform HTTP body to dictionary'''
    data = request.get_json()
    if type(data) != dict:
        abort(400, {'message': 'Not a JSON'})
    if 'name' not in data:
        abort(400, {"message": "Missing name"})
    new_state = State(**data)
    storage.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<path:state_id>', methods=["PUT"],
                 strict_slashes=False)
def put_state(state_id):
    '''Updates a State object'''
    data_state = storage.get(State, state_id)
    if data_state is None:
        abort(404)
    data = request.get_json()
    if type(data) != dict:
        abort(400, {'message': 'Not a JSON'})
    for key, value in data.items():
        if key not in ["id", "state_id", "creates_at", "update_at"]:
            setattr(data_state, key, value)
    storage.save()
    return jsonify(data_state.to_dict()), 200
