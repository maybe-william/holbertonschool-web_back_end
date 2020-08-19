#!/usr/bin/env python3
"""
Auth Flask App
"""


import json
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from auth import Auth


AUTH = Auth()
app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.route("/", methods=['GET'], strict_slashes=False)
def root_route() -> str:
    """ get the root route
    """
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'], strict_slashes=False)
def register_route() -> str:
    """ get the root route
    """
    body = request.form

    try:
        user = AUTH.register_user(body['email'], body['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
