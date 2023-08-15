#!/usr/bin/env python3
"""
Basic Flask app module
"""

from flask import Flask, jsonify
from auth import Auth


Auth = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """ GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users(password: str = None, email: str = None):
    """ POST /users
    Return:
      - JSON payload
    """
    try:
        user = Auth.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
