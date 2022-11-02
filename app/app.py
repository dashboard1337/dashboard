# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/source')
def source():
    return redirect('https://github.com/AltDaze/dashboard')


if __name__ == "__main__":
    app.run(debug=True)
