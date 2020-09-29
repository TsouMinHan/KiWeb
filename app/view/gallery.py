from flask import render_template, request, jsonify
from flask_login import login_required
from datetime import datetime

from ..models import GalleryDB, BahaImgListDB
from . import main

db= GalleryDB()
list_db = BahaImgListDB()

global img_ls

@main.route('/gallery', methods=['GET', 'POST'])
@login_required
def gallery_index():
    global img_ls
    img_ls = db.get_img_ls()

    return render_template('gallery.html', data={"img_ls": img_ls})

@main.route('/data_from_adax', methods=['POST'])
def gallery_done():
    global img_ls

    mode = request.get_json()['mode']
    db.delete_img(img_ls)

    if mode == 'done':
        img_ls = db.get_img_ls()
        return jsonify({"img_ls": img_ls})

    return jsonify({})

def find_same_url(url):
    log = list_db.get_record()

    if url in log:            
        return True
    return False

@main.route("/baha_gallery_ajax", methods=["POST"])
def baha_gellery_ajax():
    data = request.get_json()

    url = data["url"]    

    # check if url in the list or not
    if not find_same_url(url):
        list_db.add(url)
        status = "OK"

    else:
        status = "Failed"
    
    return jsonify({"status": status})