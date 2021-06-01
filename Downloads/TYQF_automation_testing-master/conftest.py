#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/5/16 4:53 下午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : conftest.py
import allure
import pytest

from browser import Browser
from utils import load_env

browser = None

print("I am running!")

@pytest.fixture(scope='session', autouse=True)
def browser_init():
    print("browser_init session")
    global browser
    if browser is None:
        browser = Browser()
    return browser


@pytest.fixture(scope="class")
def get_pc_main_page_with_no_logged(browser_init):
    print("loggin_with_no-logged class")
    main_page = browser_init.launch()
    yield main_page
    browser_init.quit()


@pytest.fixture(scope="class")
def get_pc_main_page_with_logged(browser_init):
    print("loggin_with_logged class")
    env = load_env()
    username = env['pc'][env['default']]['username']
    password = env['pc'][env['default']]['password']
    main_page = browser_init.launch().go_to_login().login_successfully(username, password)
    yield main_page
    browser_init.quit()


@pytest.fixture(scope="class")
def get_seller_main_page(browser_init):
    print("seller-main-page function")
    env = load_env()
    username = env['seller'][env['default']]['username']
    password = env['seller'][env['default']]['password']
    main_page = browser_init.launch(test_end='seller').login_successfully(username, password)
    yield main_page
    browser_init.quit()


@pytest.fixture(scope="class")
def get_om_main_page(browser_init):
    print("om-main-page module")
    env = load_env()
    username = env['om'][env['default']]['username']
    password = env['om'][env['default']]['password']
    main_page = browser_init.launch(test_end='om').login_successfully(username, password)
    yield main_page
    browser_init.quit()


@pytest.fixture(scope='function', autouse=True)
def capture_screenshot(browser_init):
    print("capture_screen function")
    yield
    # todo: check sys.exc_info没有获取异常的原因
    # print('sys里有没有错误信息:{0}'.format(sys.exc_info()))
    # if sys.exc_info()[0]:
    screenshot = browser_init.driver.get_screenshot_as_png()
    allure.attach(screenshot, '截图', allure.attachment_type.PNG)


