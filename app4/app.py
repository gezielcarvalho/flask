import os
from flask import request
from config import login_manager, app, db

@app.route('/')
def hello():
    return "Hello!"


if __name__ == '__main__':
    app.run(debug = True)