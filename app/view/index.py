from flask import render_template, request, jsonify, flash
from flask_login import login_required

import twder # 匯率套件

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
    print(key_id)

    return jsonify(bm.get_record())

@main.route('/index_ajax', methods=['GET', 'POST'])
def index_ajax():
    data = request.get_json() 
    results = dict()
    url = data['url'] ## input url
    print(url, '-'*10)
    res = bookmark_crawler.get_requests(url)

    if res:
        soup = bookmark_crawler.get_soup(res)
        
        title = bookmark_crawler.get_title(soup)
        favicon = bookmark_crawler.get_favicon(res)
        results[title] = {
            "url": url,
            "favicon": favicon
        }
        data = bm.insert(results)
    else:
        results['flash'] = f'{url} not correct!!'

    return jsonify(results)

@main.route('/exchange_money_ajax', methods=['GET', 'POST'])
def exchange_money_ajax():
    data = request.get_json() 
    results = dict()

    currency = data['currency']
    money = int(data['money'])

    rate = eval(twder.now(currency)[3])

    results['result'] = money*rate
    results['rate'] = rate
    print(results['result'], results['rate'])

    return jsonify(results)