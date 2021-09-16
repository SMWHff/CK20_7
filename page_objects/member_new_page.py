# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : member_new_page.py
# @Time       : 2021/9/16 18:36
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NewMemberPage(BasePage):
    """
    新建成员界面类
    """
    _base_activity = ".contact.controller.ContactAddFastModeActivity"

    def new_member(self, name, phone):
        """
        新建成员到通讯录中
        :param name: 姓名
        :param phone: 手机
        :return: 返回通讯录界面类
        """
        # 为防止循环引用，在方法内部导入包
        from page_objects.addmember_page import AddMemberPage
        # 输入姓名
        self.driver.find_element(By.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(name)
        # 输入手机号
        self.driver.find_element(By.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText").send_keys(phone)
        # 点击保存
        self.driver.find_element(By.XPATH, "//*[@text='保存']").click()
        # 跳转到添加成员界面
        return AddMemberPage(self.driver, self.dict_data)
