#!/usr/bin/python3
""" Flask app that display HBNB page
    on route /hbnb_filters
"""
from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """Loads HBNB page with populated filters"""
    amenities = storage.all(Amenity)
    states = storage.all(State)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down(td):
    """close session when application context in popped"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
