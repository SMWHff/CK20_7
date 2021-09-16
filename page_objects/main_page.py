# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : main_page.py
# @Time       : 2021/9/12 20:07
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.contacts_page import ContactsPage


class MainPage(BasePage):
    """
    主界面类
    """
    _base_activity = ".launch.WwMainActivity"

    def goto_contacts(self):
        """
        跳转到通讯录界面
        :return: 返回通讯录界面类
        """
        # 点击通讯录按钮
        self.find(By.XPATH, "//*[@text='通讯录']").click()
        return ContactsPage(self.driver, self.dict_data)
