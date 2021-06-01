#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
# @Time    : 2021/4/20 10:06 上午
# @Author  : 姜晖
# @Email   : jianghui@tianyancha.com
# @File    : base_page.py

from contextlib import contextmanager

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

    """
    实现通用的Page方法，对常用自动化行为做封装
    减少每个Page对Appium，selenium等库的太多依赖
    """
    # 此处是黑名单机制，任何广告弹窗，tips等等都可以定义在这，形式如下：
    # [(By.ID, "image_cancel"),(By.ID, "tips")                   ]
    _black_list = [(By.CLASS_NAME, "close-btn")]

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find_element(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            # 按理说应该这块是递归调用，但是这块要慎重处理，处理不好的话会出现死循环
            #self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_elements(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
            return self.driver.find_elements(*locator)
        except:
            self.handle_exception()
            # 按理说应该这块是递归调用，但是这块要慎重处理，处理不好的话会出现死循环
            #self.find_element(locator)
            return self.driver.find_elements(*locator)

    # 此方法的好处是不仅仅在找元素的时候，处理异常，同时在点击的时候遇到任何问题，也会去看看是不是有什么干扰项。
    def find_element_and_click(self, locator):
        try:
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def find_element_and_input(self, locator, keyword):
        try:
            self.find_element(locator).clear()
            self.find_element(locator).send_keys(keyword)
        except:
            self.handle_exception()
            self.find_element(locator).clear()
            self.find_element(locator).send_keys(keyword)

    def get_current_url(self) -> str:
        """
        get current url of opening page
        """
        return self.driver.current_url

    @contextmanager
    def wait_for_page_load(self, element: WebElement = None):
        """
        Wait until page loaded, if element assigned, wait specific element loaded and otherwise wait full page
        :param element:
        :return:
        """
        old_page = self.driver.find_element_by_tag_name('html') if not element else element
        yield
        WebDriverWait(self.driver, 60).until(
            staleness_of(old_page),
            'The page {0} is not refreshed'.format(self.get_current_url())
        )

    def get_all_window_handles(self):
        return self.driver.window_handles

    def switch_to_window(self, window_name):
        self.driver.switch_to_window(window_name)

    def switch_to_div_alert(self):
        """
        This is made to handle those div kind of alert dialog
        """
        self.driver.switch_to.default_content()

    def handle_exception(self):
        for locator in self._black_list:
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                elements[0].click()
            else:
                print("%s not found" % str(locator))
            # find_elements是重隐式等待的，如果黑名单的locator有的话会点击，但是如果没有的话，也会等待隐式等待设置的时间，所以可以先判断黑名单的项是否在page_source中
            # page_source = self._driver.page_source
            # if "image_cancel" in page_source:
            #     self._driver.find_element(*locator).click()
            # elif "tips" in page_source:
            #     pass

    def get_page_source(self):
        return self.driver.page_source

    def switch_to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def get_element_attribute(self, locator, attr):
        element = self.find_element(locator)
        return element.get_attribute(attr)

    def get_elements_attribute(self, locator, attr, index=0):
        element = self.find_elements(locator)[index]
        return element.get_attribute(attr)

    def capture_screenshot_to_allure(self):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, '截图', allure.attachment_type.PNG)

    def get_local_storage(self, key):
        return self.driver.execute_script("return localStorage.getItem(arguments[0])", key)

    def set_local_storage(self, key, value):
        self.driver.execute_script("localStorage.setItem(arguments[0], arguments[1]);", key, value)

