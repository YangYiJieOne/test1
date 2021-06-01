#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 5:55 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : main_page.py
from base_page import BasePage
from selenium.webdriver.common.by import By
from seller.page.basic_setting_page import BasicSettingPage
from seller.page.shop_info_page import ShopInfoPage

class MainPage(BasePage):
    _setting_tag = (By.LINK_TEXT, '设置')
    def go_to_setting(self):
        self.find_element_and_click(self._setting_tag)
        return BasicSettingPage(self.driver)

    _shopInfo_tag = (By.CSS_SELECTOR, 'a[@text="店铺信息"]')
    def go_to_shopInfo(self):
        self.find_element_and_click(self._setting_tag)
        self.find_element_and_click(self._shopInfo_tag)
        return ShopInfoPage(self.driver)
