#!/usr/bin/python3.7
# -*- coding: UTF-8 –*-
# Author    : 杨一杰
# @Time     : 2021/5/31 8:20 下午
# @File     : shop_info_page.py


from selenium.webdriver.common.by import By
from base_page import BasePage

class ShopInfoPage(BasePage):
    _check_status = (By.CSS_SELECTOR, "span[@text='审核状态：']")
    _account_status = (By.CSS_SELECTOR, "span[@text='账号状态：']")
    _shop_status = (By.CSS_SELECTOR, "span[@text='店铺状态：']")

    def testGetCheckStatus(self):
        return None