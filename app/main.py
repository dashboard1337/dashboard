from flask import Flask, render_template
import app.auth as auth

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/register')
def register():
    return render_template('auth/signup.html')


@app.route('/dashboard')
def dashboard():
    return render_template('/dashboard/dashboard.html')


if __name__ == "__main__":
    # flask --app app/main.py --debug run
    app.run(debug=True)
