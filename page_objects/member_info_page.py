# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : member_info_page.py
# @Time       : 2021/9/16 18:17
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.member_settings_page import MemberSettingsPage


class MemberInfoPage(BasePage):
    """
    个人信息显示界面
    """
    _base_activity = ".contact.controller.ContactDetailBriefInfoProfileActivity"

    def goto_member_settings(self):
        """
        跳转到成员设置界面
        :return: 返回成员设置界面类
        """
        # 点击左上角三个点
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/top_bar_right_button1']").click()
        return MemberSettingsPage(self.driver, self.dict_data)
