#!/usr/bin/env python3
""" Handle all Session Auth routes """
import os

from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_rt():
    """
    route handle the Login Process
    setup the session
    """
    ENV = os.getenv('SESSION_NAME')
    email, pwd = request.form.get('email'), request.form.get('password')
    if email == "" or not email:
        return jsonify({'error': 'email missing'}), 400
    if pwd == "" or not pwd:
        return jsonify({'error': 'password missing'}), 400
    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if user.is_valid_password(pwd):
            from api.v1.app import auth
            session = auth.create_session(user.id)
            res = jsonify(user.to_json())
            res.set_cookie(ENV, session)
            return res
    return jsonify({"error": "wrong password"}), 401


@app_views.route('auth_session/logout', methods=['DELETE'], strict_slashes=False)
def destroy():
    """
    call the session destroy method
    """
    from api.v1.app import auth
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)