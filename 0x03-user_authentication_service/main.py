#!/usr/bin/env python3
"""
End-to-end integration test for the authentication service
"""
import requests


def register_user(email: str, password: str) -> None:
    """Test register_user
    """
    url = 'http://localhost:5000/users'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'user created'}
    print('OK', flush=True)


def log_in_wrong_password(email: str, password: str) -> None:
    """Test log_in_wrong_password
    """
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 401
    print('OK', flush=True)


def log_in(email: str, password: str) -> str:
    """Test log_in
    """
    url = 'http://localhost:5000/sessions'
    data = {'email': email, 'password': password}
    response = requests.post(url, data=data)
    assert response.status_code == 200
    assert response.json() == {'email': email, 'message': 'logged in'}
    print('OK', flush=True)
    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """Test profile_unlogged
    """
    url = 'http://localhost:5000/profile'
    response = requests.get(url)
    assert response.status_code == 403
    print('OK', flush=True)


def 


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


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
