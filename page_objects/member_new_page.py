# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : member_new_page.py
# @Time       : 2021/9/16 18:36
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class NewMemberPage(BasePage):
    """
    新建成员界面类
    """
    _base_activity = ".contact.controller.ContactAddFastModeActivity"
    _locator_name = (By.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText")
    _locator_phone = (By.XPATH, "//*[contains(@text, '手机')]/..//android.widget.EditText")
    _locator_save = (By.XPATH, "//*[@text='保存']")
    _locator_toast = (By.XPATH, "//android.widget.Toast")
    _locator_dialog = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/custom_dialog_msg']")
    _locator_ok = (By.XPATH, "//*[@text='确定']")

    def new_member(self, name, phone):
        """
        新建成员到通讯录中成功
        :param name: 姓名
        :param phone: 手机
        :return: 返回通讯录界面类
        """
        # 为防止循环引用，在方法内部导入包
        from page_objects.addmember_page import AddMemberPage
        # 输入姓名
        self.find(self._locator_name).send_keys(name)
        # 输入手机号
        self.find(self._locator_phone).send_keys(phone)
        # 点击保存
        self.find(self._locator_save).click()
        # 跳转到添加成员界面
        return AddMemberPage(self.driver, self.dict_data)

    def new_member_fail(self, name, phone):
        """
        新建成员到通讯录中失败
        :param name: 姓名
        :param phone: 手机
        :return: 返回通讯录界面类
        """
        # 输入姓名
        self.find(self._locator_name).send_keys(name)
        # 出现 Toast 则直接返回提示内容
        list_element = self.finds(self._locator_toast)
        if len(list_element) > 0:
            return list_element[0].text
        # 输入手机号
        self.find(self._locator_phone).send_keys(phone)
        # 点击保存
        self.find(self._locator_save).click()
        # 返回弹窗内容
        text = self.find(self._locator_dialog).text
        # 点击关闭弹窗
        self.find(self._locator_ok).click()
        return text
