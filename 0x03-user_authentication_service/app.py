#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request, abort, make_response, redirect
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    """
    Endpoint where users can signup
    :return: json message
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """
    endpoint where users can log in
    :return: response with cookies session id or 401
    """
    email = request.form.get('email')
    pwd = request.form.get('password')
    status = AUTH.valid_login(email, pwd)
    if not status:
        abort(401)
    session = AUTH.create_session(email)
    response = make_response(jsonify({"email": f"{email}",
                                      "message": "logged in"}))
    response.set_cookie('session_id', session)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """
    :return: None
    """
    session = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'])
def profile():
    """
    Endpoint get user profile by session_id
    :return: user email or 403
    """
    session = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session)
    if user:
        return jsonify({"email": f"{user.email}"}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
