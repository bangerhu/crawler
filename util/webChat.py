# 发送企业微信通知
import json

import requests


def notice(content):
    headers_port = {
        'Content-Type': 'application/json'
    }
    dict_data = {
        'msgtype': 'text',
        'text': {
            'content': content
        }
    }

    requests.post(
        url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e6ba6fd8-e85e-4e3e-abeb-13297a48ade3',
        headers=headers_port, data=json.dumps(dict_data))
