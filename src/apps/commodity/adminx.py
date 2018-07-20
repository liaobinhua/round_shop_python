#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Wed Jul 18 13:08:35 2018
# File Name:commodity/adminx.py
# Description:

import xadmin
from .models import Commodity, CommodityImage, CommodityCategory
from .models import CommodityImage, CommodityCategoryBrand, Banner, IndexAd
from .models import HotSearchWords


class CommodityAdmin(object):
    list_display = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num',
                    'marke_price', 'shop_price', 'goods_desc', 'is_new',
                    'is_hot', 'add_time']
    search_fields = ['name']
    list_editable = ['is_hot']
    list_filter = ['name', 'click_num', 'sold_num', 'fav_num', 'goods_num',
                   'marke_price', 'shop_price', 'is_new', 'is_hot',
                   'category__name']
    style_fields = {'goods_desc': 'uditor'}

    class CommodityImageInline(object):
        model = CommodityImage
        exclude = ['add_time']
        extra = 1
        style = 'tab'

    inlines = [CommodityImageInline]


class CommodityCategoryAdmin(object):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name']


class CommodityBrandAdmin(object):
    list_display = ['category', 'image', 'name', 'desc']

    def get_context(self):
        context = super(CommodityBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = CommodityCategory.\
                objects.filter(category_type=1)
            return context


class BannerCommodityAdmin(object):
    list_display = ["goods", "image", "index"]


class HotSearchAdmin(object):
    list_display = ["keywords", "index", "add_time"]


class IndexAdAdmin(object):
    list_display = ["category", "goods"]


xadmin.site.register(Commodity, CommodityAdmin)
xadmin.site.register(CommodityCategory, CommodityCategoryAdmin)
xadmin.site.register(Banner, BannerCommodityAdmin)
xadmin.site.register(CommodityCategoryBrand, CommodityBrandAdmin)

xadmin.site.register(HotSearchWords, HotSearchAdmin)
xadmin.site.register(IndexAd, IndexAdAdmin)
