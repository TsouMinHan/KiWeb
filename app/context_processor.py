from flask import session
import os

from app import app

@app.context_processor
def inject_syntax():
    return dict(enumerate=enumerate)
