#!/usr/bin/env python3
"""
Basic Flask app module
"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def root():
    """ GET /
    Return:
      - JSON payload
    """
    return jsonify({"message": "Bienvenue"})
