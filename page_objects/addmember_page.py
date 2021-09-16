# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : addmember_page.py
# @Time       : 2021/9/12 20:19
from time import sleep
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.member_new_page import NewMemberPage


class AddMemberPage(BasePage):
    """
    添加成员界面
    """
    _base_activity = ".friends.controller.MemberInviteMenuActivity"

    def goto_addmember_by_manual(self):
        """
        跳转到新建成员界面
        :return: 返回编辑成员界面类
        """
        # 点击手动输入添加按钮
        self.driver.find_element(By.XPATH, "//*[@text='手动输入添加']").click()
        return NewMemberPage(self.driver, self.dict_data)

    def get_toast(self):
        """
        获取操作提示内容
        :return: 返回提示内容
        """
        # 强制等待 1 秒
        sleep(1)
        # 获取 Toast 提示框内容
        text = self.find(By.XPATH, "//android.widget.Toast").text
        return text
