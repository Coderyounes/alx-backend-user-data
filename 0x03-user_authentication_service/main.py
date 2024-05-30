#!/usr/bin/env python3
"""
Test Case functions
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

base = 'http://localhost:5000'
paths = ['/users', '/sessions', '/profile', 'reset_password']


def register_user(email, pwd):
    url = base + paths[0]
    data = {"email": email, "password": pwd}
    res = requests.get(url, data)
    assert res.status_code == 200
    assert res.json() == {"email": f"{email}", "message": "user created"}

# TODO: implement login in with wrong password
# TODO: implement non login hit to profile
# TODO: implement login & store the session id for further Tests
# TODO: implement profile logged using session_id
# TODO: implement logout  via session id
# TODO: implement reset token request via email & store the reset_token for further tests
# TODO: implement update_password using reset_token
# TODO: implement new Login with the new password

if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)