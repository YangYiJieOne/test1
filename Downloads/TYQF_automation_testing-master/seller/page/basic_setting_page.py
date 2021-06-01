#!/usr/bin/python3.7
# -*- coding: UTF-8 –*-
# Author    : 杨一杰
# @Time     : 2021/5/30 4:01 下午
# @File     : basic_setting_page.py


from selenium.webdriver.common.by import By
from base_page import BasePage

class BasicSettingPage(BasePage):
# 定位到店铺图片组
    _shop_img = (By.CSS_SELECTOR, "a[class='ant-upload-list-item-thumbnail']")
# 返回店铺logo中的图片url
    def getShopLogoImg(self):
        return self.get_elements_attribute(self._shop_img, 'href')
# 返回店招中的图片url
    def getShopImg(self):
        return self.get_elements_attribute(self._shop_img, 'href', 1)