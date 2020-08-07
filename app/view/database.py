from flask import render_template, request, jsonify, flash, session, url_for, redirect
from flask_login import login_required

from app.models import MainDB
from . import main



db = MainDB()

def check_data(row):
    d = request.form.get(row[1])

    if d:
        return f"'{d}'"
    return "''"

@main.route('/database/', methods=['GET', 'POST'])
@main.route('/database/<table_name>', methods=['GET', 'POST'])
# @login_required
def database_index(table_name=""):    
    table_ls = db.get_table_ls()

    page = request.args.get("page", default = 0, type = int)

    if request.method == 'POST':
        column_str = ", ".join([ row[1] for row in session["table"]["column_info_ls"]][1:]) # get column's name and remove id column.
        data_str = ", ".join(list(map(check_data, session["table"]["column_info_ls"][1:])))
        
        db.insert(session["table"]["table_name"], column_str, data_str)

    try:
        if session["table"]["table_name"] != table_name:
            session["table"] = {
                "table_name": table_name,
                "length": db.get_rows_len(table_name),
                "column_info_ls": db.get_column_ls(table_name),
            }

        column_data_ls = db.get_record(session["table"]["table_name"], page*100)

    except:
        session["table"] = {
            "table_name": "",
            "length": 0,
            "column_info_ls": [],
        }
        column_data_ls = []

    data = {
        "table_ls": table_ls,
        "column_info_ls": session["table"]["column_info_ls"],
        "table_name": session["table"]["table_name"],
        "column_data_ls": column_data_ls,
        "page": page,
        "data_length": session["table"]["length"]
    }

    return render_template('database.html', data=data)

def generate_update_sql(t):
    return f"{t[0]}={t[1]}" # check_data has given t[1] ''

@main.route('/database/<table_name>/<id>', methods=['GET', 'POST'])
def modify_index(table_name, id):

    if request.method == "POST":
        if request.form.get("update"):
            name_ls = [ row[1] for row in session["table"]["column_info_ls"][1:]]
            res_ls = list(map(check_data, session["table"]["column_info_ls"][1:]))

            sql = ", ".join(list(map(generate_update_sql, list(zip(name_ls, res_ls)))))
            
            db.update(session["table"]["table_name"], sql, id)

        elif request.form.get("delete"):
            db.delete(session["table"]["table_name"], id)

        return redirect(url_for("main.database_index", table_name=session["table"]["table_name"]))
    data = {
        "column_info_ls": session["table"]["column_info_ls"],
        "table_name": session["table"]["table_name"],
        "column_data": db.search(session["table"]["table_name"], id),
        "data_length": session["table"]["length"]
    }

    return render_template('modify.html', data=data)

