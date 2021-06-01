#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/22 2:28 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : test.py
import os
import pickle
# import time
#
# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.get("http://pc.test.tianyanqifu.com")
# driver.implicitly_wait(20)
# driver.find_element_by_css_selector('.top_login').click()
# #time.sleep(3)
# driver.find_element_by_id('account').send_keys('15810629253')
# driver.find_element_by_id('password').send_keys('Sig#tianyanqifu')
# driver.find_element_by_css_selector('button[type="submit"]').click()
# time.sleep(3)
#
# login_storage = driver.execute_script("return localStorage.getItem('b2b-pc@login')")
# print(login_storage)
# driver.quit()
# # cookies = {
# # "sajssdk_2015_cross_new_user": 1,
# # "main_url": "http%3A%2F%2Fpc.test.tianyanqifu.com%2F",
# # "WM_UUID": "3dee03ea-e419-4922-8dc1-0933bc1401ac",
# # "sensorsdata2015jssdkcross": "%7B%22distinct_id%22%3A%228a8290c0795f14f001795f884ca90035%22%2C%22first_id%22%3A%22179703f105c362-0cef624b9ce37c-37607201-1296000-179703f105d6ad%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179703f105c362-0cef624b9ce37c-37607201-1296000-179703f105d6ad%22%7D"
# # }
# # driver.add_cookie({'name': "sajssdk_2015_cross_new_user", 'value': cookies['sajssdk_2015_cross_new_user']})
# # driver.add_cookie({"name": "main_url", "value": "http%3A%2F%2Fpc.test.tianyanqifu.com%2F"})
# # driver.add_cookie({'name': "WM_UUID", "value": "3dee03ea-e419-4922-8dc1-0933bc1401ac"})
# # driver.add_cookie({"name": "sensorsdata2015jssdkcross", "value": "%7B%22distinct_id%22%3A%228a8290c0795f14f001795f884ca90035%22%2C%22first_id%22%3A%22179703f105c362-0cef624b9ce37c-37607201-1296000-179703f105d6ad%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179703f105c362-0cef624b9ce37c-37607201-1296000-179703f105d6ad%22%7D"})
# driver = webdriver.Chrome()
# driver.get("http://pc.test.tianyanqifu.com")
# time.sleep(5)
# driver.execute_script("localStorage.setItem('b2b-pc@login', arguments[0]);", login_storage)
# time.sleep(3)
# driver.get("http://pc.test.tianyanqifu.com/user-info")
import yaml

env = yaml.safe_load(open('env.yml'))
print(env)
data = {
    "schema": "http",
    "method": "get",
    "url": "http://docker.testing-studio.com:10000/demo64.txt"
}

data["url"] = str(data["url"]).replace("docker.testing-studio.com", env['docker.testing-studio.com'][env['default']])
print(data["url"])


# 如何通过字典生成对应的yml文件
# env = {
#     "docker.testing-studio.com": {
#         "dev": "127.0.0.1",
#         "test": "1.1.1.2",
#         "level": 4
#     },
#     "default": "dev"
# }
# env_yml = yaml.safe_dump(env)
# print(env_yml)
