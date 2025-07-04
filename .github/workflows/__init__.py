
"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask application startup')

Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'


import FlaskWebProject.views
