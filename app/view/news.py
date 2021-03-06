from flask import render_template, request, jsonify
from datetime import datetime, timedelta
from flask_login import login_required

from app.models import NewsDB
from . import main

db= NewsDB()

@main.route('/goClick', methods=['GET', 'POST'])
def goClick():
    res = request.get_json()
    db.update_seen(res['id'])

    return jsonify({"status": "OK"})

@main.route('/news', methods=['GET', 'POST'])
@login_required
def news_index():
    date = "" # get the show cloumn is 0.
    if request.args.get('date'):
        date = request.args.get('date')
    # else:
        # date = datetime.now().date() - timedelta(days=1)
        

    record_dc = db.get_record(date)

    return render_template('news.html',
                            record_dc=record_dc,
                            date=date)