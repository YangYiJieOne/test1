#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 3:58 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : search_page.py
from selenium.webdriver.common.by import By

from base_page import BasePage


class SearchPage(BasePage):

    _input_search_text = (By.ID, 'search')

    def get_search_text(self):
        return self.get_element_attribute(self._input_search_text, 'value')
