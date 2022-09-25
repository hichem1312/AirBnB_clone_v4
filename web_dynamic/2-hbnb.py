#!/usr/bin/python3
"""This is module 10-hbnb_filters
In this module we combine flask with sqlAlchemy for the first time
Run this script from AirBnB_v2 directory for imports"""
from flask import Flask, render_template
from models import storage
import uuid
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/2-hbnb')
def display_hbnb():

    states = storage.all('State')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    cache_id = uuid.uuid4()
    return render_template('2-hbnb.html',
                           states=states,
                           amenities=amenities,
                           places=places,
                           cache_id=cache_id)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)