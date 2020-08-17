from bs4 import BeautifulSoup
from pathlib import Path
import requests

def get_requests(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res
    return None

def get_soup(res):
    return BeautifulSoup(res.text, 'html.parser')

def get_title(soup):
    title = soup.title
    if title:
        return title.text

    return "No title" 

def get_favicon(res):
    path_url = res.request.path_url
    favico_url = res.url + '/favicon.ico'
    if path_url!='/':
        favico_url = favico_url.replace(path_url, '')
        
    res = requests.get(favico_url)
    if res.status_code==200:
        return favico_url
    return ""

if __name__ == '__main__':
    res = get_requests("https://forum.gamer.com.tw/A.php?bsn=60076")
    a = get_favicon(res)
    print(a)