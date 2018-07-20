#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Wed Jul 18 09:07:12 2018
# File Name:users/adminx.py
# Description:

import xadmin
from xadmin import views
from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "ShoppingGo"
    site_footer = "round_shop"


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', 'add_time']


xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
