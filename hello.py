#! /usr/env/bin python3
"""A quick test of the Flask framework."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Prints 'Hello, World!'."""
    return 'Hello, World!'
