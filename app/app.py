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


# @app.route('/auth')
# def auth():
#     return redirect(url_for('login'))
#
#
# @app.route('/auth/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         # login and password verification if true else abort(401)
#         return redirect(url_for(f'dashboard/{username}'))
#     return render_template('auth/login.html', error=error)

    # Authorization code example
    # error = None
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # return render_template('login.html', error=error)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

# @app.route('/feedback', methods=["POST", "GET"])
# def feedback():
#     if request.method == 'POST':
#         #  todo: add checker + else 'error sent'
#         flash("message's sent")


if __name__ == "__main__":
    app.run(debug=True)
