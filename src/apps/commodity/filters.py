#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Fri Jul 20 21:51:30 2018
# File Name:filters.py
# Description:

import django_filters
from django.db.models import Q

from .models import Commodity


class CommodityFilter(django_filters.rest_framework.FilterSet):
    """
    商品的过滤类
    """
    pricemin = django_filters.NumberFilter(field_name='shop_price',
                                           help_text="最低价格",
                                           lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price',
                                           help_text='最高价格',
                                           lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(
            Q(category_id=value)|
            Q(category__parent_category_id=value)|
            Q(category__parent_category__parent_category_id=value)
        )

    class Meta:
        model = Commodity
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
