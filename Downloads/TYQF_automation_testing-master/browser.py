#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 12:18 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : browser.py
from base_page import BasePage
from selenium import webdriver

from pc.page.main_page import MainPage
from seller.page.login_page import LoginPage as seller_login
from om.page.login_page import LoginPage as om_login
from utils import load_env


class Browser(BasePage):
    """
    web浏览器操作，包含启动，退出等
    """

    def launch(self, test_end='pc'):
        self.driver = webdriver.Chrome()
        env = load_env()
        url = env[test_end.lower()][env['default']]['url']
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        if test_end.lower() == 'pc':
            return MainPage(self.driver)
        elif test_end.lower() == 'seller':
            return seller_login(self.driver)
        elif test_end.lower() == 'om':
            return om_login(self.driver)

    def quit(self):
        self.driver.quit()


