# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)


#  @todo Create homepage
#  @body Make info, buttons etc.
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    # flask --app app/main.py --debug run
    app.run(debug=True)
