import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_user, logout_user, current_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A!234567'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@:localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['DEBUG'] = True

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = 'login'