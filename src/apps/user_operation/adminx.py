#!/usr/bin/python3
# encoding: utf-8
# Author:BinhuaLiao
# Created Time:Wed Jul 18 12:51:05 2018
# File Name:user_operation/adminx.py
# Description:

import xadmin
from .models import UserFav, UserLeavingMessage, UserAddress


class UserFavAdmin(object):
    list_display = ["user", "goods", "add_time"]


class UserLeavingMessageAdmin(object):
    list_display = ['user', 'message_type', 'message', 'add_time']


class UserAddressAdmin(object):
    list_display = ['signer_name', 'signer_mobile', 'district', 'address']


xadmin.site.register(UserFav, UserFavAdmin)
xadmin.site.register(UserAddress, UserAddressAdmin)
xadmin.site.register(UserLeavingMessage, UserLeavingMessageAdmin)
