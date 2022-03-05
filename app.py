from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps


app = Flask(__name__)
app.config['SECRET_KEY'] = '4a4e10e34613490c8bc2b3b1a93120f2'


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Logged in currently!"


if __name__ == "__main__":
    app.run(debug=True)
