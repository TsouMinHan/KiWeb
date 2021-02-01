from flask import Blueprint, url_for

main = Blueprint('main', __name__)

from . import index, login, news, bookSearch, gallery, database, log, trend, capsule, company_search