from flask import render_template, request, jsonify, flash
from flask_login import login_required

from app.models import LogDB
from . import main

db = LogDB()

@main.route('/log')
@login_required
def log_index():    
    data = db.get_log()

    return render_template('log.html', data=data)

