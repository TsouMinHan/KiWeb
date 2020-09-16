from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

def get_df():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQsylRAmrxl43kbbv_MrWuzJkopLv4j6VLRJaEJrrL0I4ERSihG5w84ueG6j6qx2OxDcQmYXJF2c-9g/pubhtml?gid=0&single=true"

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    tr_div = soup.select("tr")[2:]
    date = tr_div[0].text

    trend_ls = []

    for ele in tr_div[1:]:
        c = []
        for i, e in enumerate(ele.select("td")[2:6]):
            c.append(e.text)
        trend_ls.append(tuple(c))

    title_ls = trend_ls[0]
    trend_ls = trend_ls[1:]

    df = pd.DataFrame(trend_ls, columns=title_ls)

    return df

def get_today_trend_dc(df):
    dc = {}

    positive_two = sum(df['今日多空趨勢比'] == '+2')
    positive_one = sum(df['今日多空趨勢比'] == '+1')
    negative_one = sum(df['今日多空趨勢比'] == '-1')
    negative_two = sum(df['今日多空趨勢比'] == '-2')

    dc["今日多空趨勢比"] = [f"+2：{positive_two}", f"+1：{positive_one}", f"-1：{negative_one}", f"-2：{negative_two}"]
    
    return dc

def get_yesterday_trend_dc(df):
    dc = {}

    positive_two = sum(df['昨日多空趨勢比'] == '+2')
    positive_one = sum(df['昨日多空趨勢比'] == '+1')
    negative_one = sum(df['昨日多空趨勢比'] == '-1')
    negative_two = sum(df['昨日多空趨勢比'] == '-2')

    dc["今日多空趨勢比"] = [f"+2：{positive_two}", f"+1：{positive_one}", f"-1：{negative_one}", f"-2：{negative_two}"]

    return dc

def get_energy_trend_dc(df):
    dc = {}

    up = sum(df['多空能量比'] == '▲ 多方')
    down = sum(df['多空能量比'] == '▼ 空方')
    middle = sum(df['多空能量比'] == '─ 持平')

    dc["多空能量比"] = [f"▲：{up}", f"▼：{down}", f"─：{middle}"]

    return dc

def get_nice_dc(df):
    dc = {}

    pasitive_two = df.loc[(df['今日多空趨勢比'] == '+2') & (df['昨日多空趨勢比'] == '+2') & (df['多空能量比'] == '▲ 多方')]['幣種'].to_string(index=False)

    pasitive_one = df.loc[(df['今日多空趨勢比'] == '+1') & (df['昨日多空趨勢比'] == '+1') & (df['多空能量比'] == '▲ 多方')]['幣種'].to_string(index=False)

    negative_one = df.loc[(df['今日多空趨勢比'] == '-1') & (df['昨日多空趨勢比'] == '-1') & (df['多空能量比'] == '▼ 空方')]['幣種'].to_string(index=False)
    negative_two = df.loc[(df['今日多空趨勢比'] == '-2') & (df['昨日多空趨勢比'] == '-2') & (df['多空能量比'] == '▼ 空方')]['幣種'].to_string(index=False)
    
    dc['建議操作'] = [f"+2 多方: {pasitive_two}", f"+1 多方: {pasitive_one}", f"-1 空方: {negative_one}", f"-2 空方: {negative_two}"]

    return dc