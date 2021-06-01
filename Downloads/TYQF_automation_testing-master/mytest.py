#!/usr/bin/python3.7
# -*- coding: UTF-8 –*-
# Author    : 杨一杰
# @Time     : 2021/5/30 2:14 下午
# @File     : mytest.py

from selenium import webdriver
from  base_page import BasePage
from selenium.webdriver.common.by import By
import yaml

def locatTest():
    try:
        dr = webdriver.Chrome()
        dr.get("https://seller.tianyanqifu.com/")
        d = BasePage(dr)
        d.find_element_and_input((By.ID, "account"), "15901563242")
        d.find_element_and_input((By.ID, "password"), "abc123456")
        d.find_element_and_click((By.CSS_SELECTOR, "button"))
        d.find_element_and_click((By.LINK_TEXT, "设置"))
        d.find_element_and_click((By.LINK_TEXT, "店铺信息"))

        statusList = d.find_elements((By.CSS_SELECTOR, 'div[class="ant-col ant-col-8"]'))
        for e in statusList:
            print(e.text[:-2])
    finally:
        dr.quit()

# file = "./seller/data/shopInfoData.yml"
# file = yaml.safe_load(open(file, 'r'))
# print(type(file), file)

if __name__ == '__main__':
    locatTest()


