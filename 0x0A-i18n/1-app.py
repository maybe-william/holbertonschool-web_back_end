#!/usr/bin/env python3
"""
Flask App
"""


import json
from flask import Flask
from flask import render_template
from flask_babel import Babel


class Config(object):
    """A babel configuration object"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route("/", methods=['GET'], strict_slashes=False)
def root_route() -> str:
    """ get the root route
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
