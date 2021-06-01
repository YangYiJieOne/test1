#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 4:44 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : test_search.py
import pytest
import yaml
import allure


@pytest.mark.usefixtures("get_pc_main_page_with_no_logged")
@allure.feature("非登录状态下查看搜索功能")
class TestSearchWithNoLogged:
    @allure.story("未登录查看搜索数据")
    @pytest.mark.parametrize("keyword", yaml.safe_load(open('../data/searchdata.yml')))
    def test_search(self, keyword, get_pc_main_page_with_no_logged):
        search_page = get_pc_main_page_with_no_logged.search(keyword)
        assert keyword == search_page.get_search_text()


@pytest.mark.usefixtures("get_pc_main_page_with_logged")
@allure.feature("登陆状态下测试搜索功能")
class TestSearchWithLogged:
    @allure.story("登录查看搜索数据")
    @pytest.mark.parametrize("keyword", yaml.safe_load(open('../data/searchdata.yml')))
    def test_search(self, keyword, get_pc_main_page_with_logged):
        search_page = get_pc_main_page_with_logged.search(keyword)
        assert keyword == search_page.get_search_text()




