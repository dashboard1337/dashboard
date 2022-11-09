# -*- coding: utf-8 -*-

"""
TODO:
 Move all routes here
"""

from .app import app
from flask import render_template


@app.route('/')
def index():
    return render_template("index.html")