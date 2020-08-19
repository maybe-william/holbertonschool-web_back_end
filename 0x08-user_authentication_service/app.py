#!/usr/bin/env python3
"""
Auth Flask App
"""


import json
from flask import Flask, jsonify, abort, request, make_response
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
    """ get the register route
    """
    body = request.form

    try:
        user = AUTH.register_user(body['email'], body['password'])
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route("/sessions", methods=['POST'], strict_slashes=False)
def login_route() -> str:
    """ get the login route
    """
    body = request.form

    email = body.get('email', '')
    password = body.get('password', '')
    valid = AUTH.valid_login(email, password)
    if not valid:
        abort(401)
    resp = make_response(jsonify({"email": email, "message": "logged in"}))
    resp.set_cookie('session_id', AUTH.create_session(email))
    return resp


@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout_route() -> str:
    """ get the logout route
    """
    sess = request.cookies.get('session_id')
    email_and_id = AUTH.get_user_from_session_id(sess)
    if email_and_id is None:
        abort(403)
    AUTH.destroy_session(int(email_and_id.split(':')[1]))
    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
