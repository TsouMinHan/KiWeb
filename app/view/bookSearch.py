from flask import render_template, session, request, jsonify
from flask_login import login_required
from datetime import datetime
import urllib.parse
import requests
import json
import re

from . import main

url_formula_dc = {
    "google": 'https://www.google.com/search?q={}',
    "PTT 心得": 'https://www.google.com/search?q={} PTT',
    "PTT sale": 'https://www.google.com/search?q={} 售書',
    "googl_play": 'https://play.google.com/store/search?q={}&c=books',
    "tazze": 'https://www.taaze.tw/rwd_searchResult.html?keyType%5B%5D=0&keyword%5B%5D={}',
    "tenlong": 'https://www.tenlong.com.tw/search?utf8=%E2%9C%93&keyword={}',
    "Taichung Library": 'https://ipac.library.taichung.gov.tw/webpac/search.cfm?m=ss&k0={}&t0=k&c0=and',
    "Momo": 'https://www.momoshop.com.tw/search/searchShop.jsp?keyword={}',
}

hyread_dc = {
        "台中": "https://taichunggov.ebook.hyread.com.tw/searchList.jsp?search_field=FullText&search_input={}",
        "台北": "https://tpml.ebook.hyread.com.tw/searchList.jsp?search_field=FullText&search_input={}"
    }

def utf8_to_url(word):
    return urllib.parse.quote(word)

def mix_url(url_formula, keyword):
    
    return url_formula.format(utf8_to_url(keyword))

def get_result_by_hyread(url):
    res = requests.get(url)
    if res.status_code == 200:
        num = re.findall(r"<em id='totalpage'>([0-9.+])</em>件</span>", res.text)
        return num if num else 0
    return '404NotFound'

def get_dict():
    file = r".\app\static\doc\bookSearch.json"
    with open(file, encoding="utf-8") as json_file:
        data = json.load(json_file)
    
    return data['another'], data['hyread']

@main.route('/dataFromAjax', methods=['POST'])
def ajax_index():
    data = request.get_json()

    results = dict()
    title = data['keyword']
    if title:
        for key, formula in url_formula_dc.items():
            results[key] = mix_url(formula, title)
        
        for key, value in hyread_dc.items():
            url = mix_url(value, title)
            num = get_result_by_hyread(url)
            results[key+'-'+str(num)] = url

    session['bookSearch_results'] = results
    session['book_name'] = title

    return jsonify(results)
    
@main.route('/bookSearch', methods=["GET"])
@login_required
def bookSearch_index():
    results = session.get("bookSearch_results")

    if request.args.get("book_name"):
        book_name = request.args.get("book_name")
        submit_click = True
    else:
        book_name = session.get("book_name")
        book_name = book_name if book_name else ''
        submit_click = False

    data = {
        "results": results,
        "book_name": book_name,
        "submit_click": submit_click
    }
    return render_template('bookSearch.html', data=data) 