# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, flash, request, escape, url_for

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


@app.route('/<username>')
def dashboard(username):
    # return f'{username} profile'
    return render_template('dashboard.html', username=username)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        pass  # return do_the_login()
    else:
        return render_template('login.html', error=error)

    # Authorization code example
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # return render_template('login.html', error=error)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/feedback', methods=["POST", "GET"])
def feedback():
    if request.method == 'POST':
        #  todo: add checker + else 'error sent'
        flash("message's sent")


if __name__ == "__main__":
    app.run(debug=True)
