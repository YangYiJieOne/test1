#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 9:39 上午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : login_page.py
from selenium.webdriver.common.by import By
from base_page import BasePage


class LoginPage(BasePage):

    _username = (By.ID, 'account')
    _password = (By.ID, 'password')
    _submit = (By.CSS_SELECTOR, 'button[type="submit"]')
    # _submit = (By.XPATH, '//*[@type="submit"]')

    def login_successfully(self, username, password):
        from pc.page.main_page import MainPage
        self.find_element_and_input(self._username, username)
        self.find_element_and_input(self._password, password)
        self.find_element_and_click(self._submit)
        return MainPage(self.driver)

    def login_failed(self, username, password):
        self.find_element_and_input(self._username, username)
        self.find_element_and_input(self._password, password)
        self.find_element_and_click(self._submit)
        return self



