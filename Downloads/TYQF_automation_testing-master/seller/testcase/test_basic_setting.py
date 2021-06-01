#!/usr/bin/python3.7
# -*- coding: UTF-8 –*-
# Author    : 杨一杰
# @Time     : 2021/5/28 5:58 下午
# @File     : test_setting_info.py

import pytest
import yaml
import allure

# 测试设置-基本设置
# 校验点-店铺logo&店铺店招 图片Url正确
@pytest.mark.usefixtures("get_seller_main_page")
@allure.feature("验证商家基本信息")
class TestSellerBasicSettingInfo:
    _imgUrl = yaml.safe_load(open('../data/basicSettingData.yml'))
    _logo, _img = _imgUrl["logo"], _imgUrl["img"]
    @allure.story("验证店铺logo和正确")
    def testLogo(self, get_seller_main_page):
        assert self._logo == get_seller_main_page.go_to_setting().getShopLogoImg()

    def testImg(self, get_seller_main_page):
        assert self._img == get_seller_main_page.go_to_setting().getShopImg()
