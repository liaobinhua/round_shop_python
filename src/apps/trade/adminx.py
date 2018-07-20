#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Wed Jul 18 12:55:50 2018
# File Name:trade/adminx.py
# Description:

import xadmin
from .models import ShoppingCart, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ['user', 'goods', 'nums']


class OrderInfoAdmin(object):
    list_display = ['user', 'order_sn', 'trade_no', 'pay_status', 'post_script',
                    'order_mount', 'pay_time', 'add_time']

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline,]


xadmin.site.register(ShoppingCart, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
