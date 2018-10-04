from flask import Flask
from flask_cors import CORS
from server import db
from server import mongodb
from flask import request, jsonify
import json
import pytest


def create_app():
    my_app = Flask(__name__)
    return my_app


app = create_app()
cors = CORS(app, resources={
    r"/todos*": {
        "origins": "*"
    },
    r"/dropdatabase": {
        "origins": "*"
    },
    r"/healthcheck": {
        "origins": "*"
    }
    })


@app.route('/todos.get', methods=['GET'])
def todos_get():
    return json.dumps(db.get_todos(mongodb.collection))


@app.route('/todos.add', methods=['POST'])
def todo_add():
    response = db.add_todo(mongodb.collection, request.json)
    return jsonify(response)


@app.route('/todos.toggle', methods=['PUT'])
def todo_toggle():
    response = db.toggle_todo(mongodb.collection, request.json)
    return jsonify(response)


@pytest.fixture
@app.route('/todos.toggleall', methods=['PUT'])
def todo_toggle_all():
    response = db.toggle_all(mongodb.collection, request.json)
    return jsonify(response)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return 'ok', 200


@app.route('/')
def index():
    return 'Hello'
