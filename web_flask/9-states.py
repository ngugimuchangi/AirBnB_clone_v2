#!/usr/bin/python3
""" Flask app that display all
    states on route /states
    state info on route states/<id>
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Returns list of states"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Returns a specific state and its cities"""
    states = storage.all(State)
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def tear_down(td):
    """close session when application context in popped"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
