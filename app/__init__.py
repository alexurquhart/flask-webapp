from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask.ext.assets import Environment, Bundle
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask_mail import Mail
from app.models import db, user, role
from tasks import celery
import os

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
assets = Environment(app)

db.init_app(app)
celery.init_app(app)

toolbar = DebugToolbarExtension(app)

user_datastore = SQLAlchemyUserDatastore(db, user.User, role.Role)
security = Security(app, user_datastore)
mail = Mail(app)

from app import views # flake8: noqa