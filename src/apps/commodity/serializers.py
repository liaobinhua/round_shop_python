#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Fri Jul 20 12:48:36 2018
# File Name:apps/commodity/serializers.py
# Description:

from rest_framework import serializers
from commodity.models import Commodity, CommodityCategory


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = "__all__"


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = CommodityCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = CommodityCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_cat = CategorySerializer2(many=True)

    class Meta:
        model = CommodityCategory
        fields = "__all__"
