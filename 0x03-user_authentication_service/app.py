#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
auth = Auth()


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
        auth.register_user(email, pwd)
        return jsonify({"email": f"{email}", "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
