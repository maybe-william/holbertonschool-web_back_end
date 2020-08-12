#!/usr/bin/env python3
""" Module of Users views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import environ


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
    """
    email = request.form.get("email", None)
    if email is None:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get("password", None)
    if password is None:
        return jsonify({"error": "password missing"}), 400
    user = User.search({"email": email})
    if user is None or len(user) == 0:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401
    from api.v1.app import auth
    sess = auth.create_session(user.id)
    ret = jsonify(user.to_json())
    cookie_name = environ.get("SESSION_NAME", None)
    ret.set_cookie(cookie_name, sess)
    return ret


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def auth_logout() -> str:
    """ DELETE /api/v1/auth_session/logout
    Return:
        - Empty JSON and 200 status
    """
    from api.v1.app import auth
    succ = auth.destroy_session(request)
    if not succ:
        abort(404)
    return jsonify({}), 200
