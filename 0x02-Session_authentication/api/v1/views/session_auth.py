#!/usr/bin/env python3
""" Handle all Session Auth routes """
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_rt(request=None):
    # TODO: retrieve email & password from request
    # TODO:(sub) check if one of them is missing or empty return 400 & JSON string
    # TODO: retrieve User instance based on email ( use search method)
    # TODO:(sub) if no User found return 404 & json string
    # TODO:(sub) if password not correct return 401 & json String (use the is_valid_password method)
    # TODO: create a Session ID from the User instance (must import Auth class)
    #  WARNING: WATCH out circular import issue
    # TODO: use create_session method to create session id
    # TODO: return a dict representation of the User instance ( use to_json() )
    # TODO: set the cookie to response
    pass
