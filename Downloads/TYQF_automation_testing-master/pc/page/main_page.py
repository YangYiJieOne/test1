#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 3:34 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : main_page.py
from selenium.webdriver.common.by import By

from base_page import BasePage
from pc.page.login_page import LoginPage
from pc.page.search_page import SearchPage


class MainPage(BasePage):

    _search_input = (By.ID, 'search')
    _search_button = (By.CLASS_NAME, 'search_btn')
    _login = (By.CSS_SELECTOR, 'a[href="/login"]')

    def search(self, keyword):
        self.find_element_and_input(self._search_input, keyword)
        self.find_element_and_click(self._search_button)
        self.switch_to_new_window()
        return SearchPage(self.driver)

    def go_to_login(self):
        self.find_element_and_click(self._login)
        return LoginPage(self.driver)

