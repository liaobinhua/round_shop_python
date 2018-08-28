#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Fri Aug  3 15:02:13 2018
# File Name:smstools.py
# Description:

import json
import requests


class SmsTools(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = ""

    def send_sms(self, code, mobile):
        # params = {
        #     "username": "liaobinhua",
        #     "password": "lbh123456"
        # }

        # response = requests.post(self.single_send_url, data=params)
        # re_dict = json.loads(response.text)
        re_dict = {
            "code": 0,
            "msg": "whydd?"
        }
        print(re_dict)
        print(re_dict['code'])
        return re_dict


if __name__ == "__main__":
    sms_tools = SmsTools("")
    sms_tools.send_sms("2017", "")
