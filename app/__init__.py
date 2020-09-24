from flask import Flask
from flask_login import LoginManager

from logging.handlers import SMTPHandler, RotatingFileHandler
from pathlib import Path
import logging
import time
import os

from config import Config

_version = "2.4.3"

app = Flask(__name__)
app.config.from_object(Config)
login = LoginManager(app)
login.login_view = 'main.login'

from app.view import main as view_bp
from app.view.errors import bp as errors_bp
app.register_blueprint(view_bp)
app.register_blueprint(errors_bp)

from . import context_processor
from .models import models