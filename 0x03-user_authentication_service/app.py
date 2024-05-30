#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request, abort, make_response, redirect
from sqlalchemy.orm.exc import NoResultFound

from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def index():
    """
    Welcome function , basic flask function
    :return: jsn string to welcome visitors
    """
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


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """
    endpoint to generate reset token based on email
    :return: json string or 403
    """
    email = request.form.get('email')
    try:
        token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": f"{email}", "reset_token": f"{token}"}), 200


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """
    This function is an endpoint in a Flask application
    that is used to update a user's password
    :return: json string or 403
    """
    e = request.form.get('email')
    password = request.form.get('new_password')
    token = request.form.get('reset_token')
    try:
        AUTH.update_password(token, password)
    except ValueError:
        abort(403)
    return jsonify({"email": f"{e}", "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
