# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, flash, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fKdwKEDPe'

menu = [
    {'name': 'Dashboard', 'url': 'dashboard'},
    {'name': 'About', 'url': 'about'},
    {'name': 'Support', 'url': 'support'},
    {'name': 'Feedback', 'url': 'feedback'},
]


@app.route('/')
def index():
    return render_template('index.html', menu=menu)


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


@app.route('/support')
def support():
    return redirect('https://github.com/AltDaze/dashboard/issues')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        #  todo: add checker + else 'error sent'
        flash("message's sent")


if __name__ == "__main__":
    app.run(debug=True)
