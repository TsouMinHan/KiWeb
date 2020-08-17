from flask import render_template, request, jsonify, flash
from flask_login import login_required

from app import bookmark_crawler
from app.models import BookMark
from . import main

bm = BookMark()

@main.route('/')
@login_required
def index():    
    data = bm.get_record()
    
    return render_template('index.html', data=data)

@main.route('/delete_bookmark_ajax', methods=['GET', 'POST'])
def delete_bookmark_ajax():
    data = request.get_json()
    key_id = data["key_id"]
    bm.delete(key_id)

    return jsonify(bm.get_record())

@main.route('/index_ajax', methods=['GET', 'POST'])
def index_ajax():
    data = request.get_json() 
    results = dict()
    url = data['url'] ## input url
    res = bookmark_crawler.get_requests(url)

    try:
        soup = bookmark_crawler.get_soup(res)
        
        title = bookmark_crawler.get_title(soup)
        favicon = bookmark_crawler.get_favicon(res)

        results[title] = {
            "url": url,
            "favicon": favicon
        }
        data = bm.insert(results)

    except Exception as e:
        results['flash'] = f'{url} {e}'

    return jsonify(results)
