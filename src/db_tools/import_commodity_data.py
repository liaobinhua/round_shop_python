#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Tue Jul 17 18:18:17 2018
# File Name:import_commodity_data.py
# Description:

import sys
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "round_shop.settings")

import django
django.setup()

from commodity.models import Commodity, CommodityCategory, CommodityImage
from db_tools.data.product_data import row_data

for commodity_detail in row_data:
    commodity = Commodity()
    commodity.name = commodity_detail['name']
    commodity.marke_price = float(
        int(commodity_detail["market_price"].replace("￥", "").replace("元", ""))
    )
    commodity.shop_price = float(
        int(commodity_detail["sale_price"].replace("￥", "").replace("元", ""))
    )
    commodity.goods_brief = commodity_detail["desc"] if commodity_detail["desc"] is not None else ""
    commodity.goods_desc = commodity_detail["goods_desc"] if commodity_detail["goods_desc"] is not None else ""
    commodity.goods_front_image = commodity_detail["images"][0] if commodity_detail["images"] else ""
    category_name = commodity_detail["categorys"][-1]
    category = CommodityCategory.objects.filter(name=category_name)
    if category:
        commodity.category = category[0]
    commodity.save()

    for goods_image in commodity_detail["images"]:
        goods_image_instance = CommodityImage()
        goods_image_instance.image = goods_image
        goods_image_instance.goods = commodity
        goods_image_instance.save()
