# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : contacts_page.py
# @Time       : 2021/9/12 20:17
from selenium.webdriver.common.by import By
from page_objects.addmember_page import AddMemberPage
from page_objects.base_page import BasePage
from page_objects.search_page import SearchPage


class ContactsPage(BasePage):
    """
    通讯录界面类
    """
    _base_activity = ".launch.WwMainActivity"
    _locator_sum = (By.XPATH, "//*[contains(@text, '人未加入')]")

    def goto_search(self):
        """
        跳转到搜索界面
        :return: 返回搜索界面类
        """
        # 点击搜索图标
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/top_bar_right_button4']").click()
        return SearchPage(self.driver, self.dict_data)

    def goto_addmember(self):
        """
        跳转到添加成员界面
        :return: 返回添加成员界面类
        """
        # 滑动查找添加成员按钮，并点击
        self.swipe_find(By.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver, self.dict_data)
