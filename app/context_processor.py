from flask import session
import os

from app import app

# @app.context_processor
# def inject_inspirational_quotes():
# 	with open(r'app\static\doc\inspirational_quotes.txt', 'r', encoding='utf-8') as f:
# 		quotes = f.readlines()
# 	return dict(quotes=quotes)

@app.context_processor
def inject_syntax():
    return dict(enumerate=enumerate)

# @app.context_processor
# def inject_note_folder_name():
# 	path = r'app\static\doc\note'
# 	return {'note_folder_name': os.listdir(path)}

# @app.context_processor
# def inject_bahaCafeteria_data():	
	
# 	return {"bahaCafeteria_data": BahaCafeteria.get_log_data()["filter_record"]}