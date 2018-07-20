#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Thu Jul 19 11:11:51 2018
# File Name:apps/commodity/view_base.py
# Description:

import json
from django.views.generic.base import View
from commodity.models import Commodity
from django.http import HttpResponse, JsonResponse
import pdb


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view 实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Commodity.objects.all()[:10]
        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            json_dict["add_time"] = good.add_time
            json_list.append(json_dict)

        return HttpResponse(json.dumps(json_list),
                            content_type="application/json")
