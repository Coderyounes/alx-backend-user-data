#!/usr/bin/env python3
"""
Test Case functions
"""
import requests

EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"

base = 'http://localhost:5000/'
paths = ['users', 'sessions', 'profile', 'reset_password']


def register_user(email, pwd):
    url = base + paths[0]
    data = {"email": email, "password": pwd}
    res = requests.post(url, data)
    assert res.status_code == 200
    assert res.json() == {"email": f"{email}", "message": "user created"}


def log_in_wrong_password(email, pwd):
    url = base + paths[0]
    data = {"email": email, "password": pwd}
    res = requests.post(url, data)
    assert res.status_code == 400


def profile_unlogged():
    url = base + paths[2]
    res = requests.get(url)
    assert res.status_code == 403


def log_in(email, pwd):
    url = base + paths[1]
    data = {"email": email, "password": pwd}
    res = requests.post(url, data)
    assert res.status_code == 200
    assert res.json() == {"email": f"{email}", "message": "logged in"}
    return res.cookies.get('session_id')


def profile_logged(session_id):
    url = base + paths[2]
    data = {"session_id": session_id}
    res = requests.get(url, cookies=data)
    assert res.status_code == 200
    assert res.json() == {"email": EMAIL}


def log_out(session_id):
    url = base + paths[1]
    res = requests.delete(url, cookies={"session_id": session_id})
    assert res.status_code == 200
    assert res.json() == {"message": "Bienvenue"}


def reset_password_token(email):
    url = base + paths[3]
    data = {"email": email}
    res = requests.post(url, data)
    assert res.status_code == 200
    return res.json().get("reset_token")


def update_password(email, token, new_passwd):
    url = base + paths[3]
    data = {
        "email": email,
        "reset_token": token,
        "new_password": new_passwd
    }
    res = requests.put(url, data)
    assert res.status_code == 200
    assert res.json() == {"email": email, "message": "Password updated"}


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
