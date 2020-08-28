#!/usr/bin/env python3
"""
Flask App
"""


import json
from flask import Flask, jsonify, abort, request, make_response, redirect
from flask import render_template
from flask_babel import Babel


app = Flask(__name__)
app.config.from_pyfile('babel.cfg')
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def root_route() -> str:
    """ get the root route
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
