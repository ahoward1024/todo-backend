from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import db
import json

app = Flask(__name__)
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
    return json.dumps(db.get_todos())


@app.route('/todos.add', methods=['POST'])
def todo_add():
    response = db.add_todo(request.json)
    return jsonify(response)


@app.route('/todos.toggle', methods=['PUT'])
def todo_toggle():
    response = db.toggle_todo(request.json)
    return jsonify(response)


@app.route('/todos.toggleall', methods=['PUT'])
def todo_toggle_all():
    response = db.toggle_todo_all(request.json)
    return jsonify(response)


@app.route('/healthcheck', methods=['GET'])
def test():
    return 'ok', 200


@app.route('/dropdatabase', methods=['GET'])
def drop_database():
    db.drop_db()
    return 'ok', 200


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # DEBUG
    # app.run(host='0.0.0.0', debug=False) # PRODUCTION
