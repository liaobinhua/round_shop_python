#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Fri Jul 20 12:48:36 2018
# File Name:apps/commodity/serializers.py
# Description:

from rest_framework import serializers
from commodity.models import Commodity


class CommoditySerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=100)
    click_num = serializers.IntegerField(default=0)
