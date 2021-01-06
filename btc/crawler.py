# 爬虫服务
import json
import random
import time
from urllib.parse import urlencode

import requests

import util.webChat as webChat


def crawler():
    kinds = 'BTC OKB ETH BNB USDT'
    jsonRes = get_json()
    symbolList = []
    USDpriceList = []
    RMBpriceList = []
    percent_change_1hList = []
    percent_change_24hList = []
    percent_change_7dList = []

    for obj in (jsonRes['data']):
        symbol = obj['symbol']
        if symbol not in kinds:
            continue
        symbolList.append(symbol)
        price = obj['quote']["USD"]["price"]
        USDpriceList.append(price)
        RMBpriceList.append(price * 6.4619)
        percent_change_1h = str(obj['quote']["USD"]["percent_change_1h"]) + "%"
        percent_change_1hList.append(percent_change_1h)
        percent_change_24h = str(obj['quote']["USD"]["percent_change_24h"]) + "%"
        percent_change_24hList.append(percent_change_24h)
        percent_change_7d = str(obj['quote']["USD"]["percent_change_7d"]) + "%"
        percent_change_7dList.append(percent_change_7d)
    data = {'Kind': symbolList, 'USD': USDpriceList, 'Rmb': RMBpriceList,
            '1hour': percent_change_1hList, '24hour': percent_change_24hList,
            '7day': percent_change_7dList}

    print(json.dumps(data))
    try:
        webChat.notice(json.dumps(data))
    except Exception:
        print("有问题")
    else:
        print("成功")


def get_json():
    baseUrl = 'https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
    headers = {'accept': 'application/json, text/plain, */*',
               'accept-encoding': 'gzip, deflate, br',
               'accept-language': 'zh-CN,zh;q=0.9,und;q=0.8',
               'origin': 'https://coinmarketcap.com',
               'referer': 'https://coinmarketcap.com/',
               'sec-fetch-dest': 'empty',
               'sec-fetch-mode': 'cors',
               'sec-fetch-site': 'same-site',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

    data = {
        'limit': 100
    }
    url = baseUrl + urlencode(data)
    response = requests.get(url, headers=headers, verify=False)
    time.sleep(50 + random.random())
    return response.json()
