from datetime import datetime, timedelta
from flask import render_template, session, request, jsonify
from flask_login import login_required

from . import main
from app.models import NewsDB

db= NewsDB()

@main.route('/goClick', methods=['GET', 'POST'])
def goClick():
    res = request.get_json()
    db.update_seen(res['id'])

    return jsonify({"status": "OK"})

@main.route('/news', methods=['GET', 'POST'])
# @login_required
def news_index():
    date = "'"
    if request.args.get('date'):
        date = request.args.get('date')
    else:
        date = datetime.now().date() - timedelta(days=1)

    record_dc = db.get_record(date)

    return render_template('news.html',
                            record_dc=record_dc,
                            date=date)