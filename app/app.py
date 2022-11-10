# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, flash, request, escape, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fKdwKEDPe'


@app.route('/')
def index():
    return render_template('dashboard/index.html')


@app.route('/dashboard/')
@app.route('/dashboard/<string:username>', methods=['GET'])
def dashboard(username=None):
    # return f'{username} profile'
    # username = email without @mail.com
    if username:
        return render_template('dashboard/dashboard.html', username=username)
    else:
        return redirect(url_for('login'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
