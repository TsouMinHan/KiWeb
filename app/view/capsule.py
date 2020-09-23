from flask import render_template
from flask_login import login_required

from . import main
from app.models import CapsuleDB

db = CapsuleDB()

def sort_output_data(capsule_ls):
    output_ls = []
    temp_ls = []

    for i, c in enumerate(capsule_ls):
        if i % 5 ==0:
            output_ls.append(temp_ls)
            temp_ls = []
        else:
            temp_ls.append(c)
    return output_ls

@main.route('/capsule', methods=["GET"])
@login_required
def capsule_index():
    capsule_ls = db.get_record()
    db.set_seen()

    return render_template('capsule.html', data=sort_output_data(capsule_ls)) 