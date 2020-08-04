from user_agent import generate_user_agent
from traceback import print_exc
from bs4 import BeautifulSoup
import requests
import json
import re

class BahaImg:
    def __init__(self, url, init_txt=''):
        self.url = url
        self.init_txt = init_txt
        self.pre_send_txt_ls = [init_txt] if init_txt else []

        self.session = requests.Session()

    def get_res(self, url):
        headers = {
            'user-agent': generate_user_agent()
        }
        with self.session.get(url, headers=headers) as res:
            pass
        if res.status_code == 200:
            return res

        self.add_to_pre_send_txt_ls(f'request {self.url} faild request code : {res.status_code}')
        return None

    def get_soup(self, res):
        if res:
            return BeautifulSoup(res.text, 'html.parser')
        return None

    def main_process(self):
        res = self.get_res(self.url)
        soup = self.get_soup(res)

        self.title = soup.find('h1').text

    def add_to_pre_send_txt_ls(self, msg):
        self.pre_send_txt_ls.append(msg)

    def run(self):
        try:
            self.main_process()

        except Exception as e:
            print_exc()
            self.add_to_pre_send_txt_ls(f'{e}')

        return '\n'.join(self.pre_send_txt_ls)
