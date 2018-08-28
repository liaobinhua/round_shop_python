#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Wed Jul 18 08:37:17 2018
# File Name:import_category_data.py
# Description:

# 独立使用Django的model
import sys
import os
import pdb


# pwd = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(pwd+"../")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "round_shop.settings")

import django
django.setup()

from commodity.models import CommodityCategory
from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_intance = CommodityCategory()
    lev1_intance.code = lev1_cat["code"]
    lev1_intance.name = lev1_cat["name"]
    lev1_intance.category_type = 1
    lev1_intance.save()

    for lev2_cat in lev1_cat["sub_categorys"]:
        lev2_intance = CommodityCategory()
        lev2_intance.code = lev2_cat["code"]
        lev2_intance.name = lev2_cat["name"]
        lev2_intance.category_type = 2
        lev2_intance.parent_category = lev1_intance
        lev2_intance.save()

        for lev3_cat in lev2_cat["sub_categorys"]:
            lev3_intance = CommodityCategory()
            lev3_intance.code = lev3_cat["code"]
            lev3_intance.name = lev3_cat["name"]
            lev3_intance.category_type = 3
            lev3_intance.parent_category = lev2_intance
            lev3_intance.save()
