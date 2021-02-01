from flask import render_template, session, request, jsonify
from flask_login import login_required
from datetime import datetime
import urllib.parse
import requests
import json
import re

from . import main

url_formula_dc = {
    "PTT Tech Job": "https://www.ptt.cc/bbs/Tech_Job/search?q={}",
    "PTT Soft Job": "https://www.ptt.cc/bbs/Soft_Job/search?q={}",
    "good job": "https://www.goodjob.life/search?q={}",
    "ursalary": "http://www.ursalary0.com/salaries/salary_lists_tw/q:{}",
    "qollie": "https://www.qollie.com/search?keyword={}&kind=company&from=banner"
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

@main.route('/companySearchAjax', methods=['POST'])
def company_search_ajax_index():
    data = request.get_json()

    results = dict()
    title = data['keyword']
    if title:
        for key, formula in url_formula_dc.items():
            results[key] = mix_url(formula, title)

    session['companySearch_results'] = results
    session['company_name'] = title

    return jsonify(results)
    
@main.route('/companySearch', methods=["GET"])
@login_required
def company_index():
    results = session.get("companySearch_results")

    if request.args.get("company_name"):
        company_name = request.args.get("company_name")
        submit_click = True
    else:
        company_name = session.get("company_name")
        company_name = company_name if company_name else ""
        submit_click = False

    data = {
        "results": results,
        "company_name": company_name,
        "submit_click": submit_click
    }
    return render_template("companySearch.html", data=data) 