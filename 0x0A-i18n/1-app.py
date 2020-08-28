#!/usr/bin/env python3
"""
Flask App
"""


import json
from flask import Flask, jsonify, abort, request, make_response, redirect
from flask import render_template
from flask_babel import Babel
from flask import Response


app = Flask(__name__)


class Config:
    """A babel configuration object"""

    LANGUAGES = ["en", "fr"]


@app.route("/", methods=['GET'], strict_slashes=False)
def root_route() -> Response:
    """ get the root route
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.config.from_object('1-app.Config')
    babel = Babel(app)
    app.run(host="0.0.0.0", port="5000")
