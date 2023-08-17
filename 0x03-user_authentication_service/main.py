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