# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : member_settings_page.py
# @Time       : 2021/9/16 18:24
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class MemberSettingsPage(BasePage):
    """
    个人信息设置界面
    """
    _base_activity = ".contact.controller.ContactDetailSettingActivity"

    def goto_editmember(self):
        """
        跳转到编辑成员界面
        :return: 返回编辑成员界面类
        """
        from page_objects.member_edit_page import EditMemberPage
        # 点击编辑成员按钮
        self.find(By.XPATH, "//*[@text='编辑成员']").click()
        return EditMemberPage(self.driver, self.dict_data)
