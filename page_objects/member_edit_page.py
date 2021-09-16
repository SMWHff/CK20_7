# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : member_edit_page.py
# @Time       : 2021/9/12 20:22
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class EditMemberPage(BasePage):
    """
    编辑成员界面类
    """
    _base_activity = ".contact.controller.ContactEditActivity"

    def del_member(self):
        """
        删除成员
        :return: 返回管理通讯录界面类
        """
        # 为防止循环引用，在方法内部导入包
        from page_objects.search_page import SearchPage
        # 滑动查找删除成员元素
        element = self.swipe_find(By.XPATH, "//*[@text='删除成员']")
        # 点击删除成员
        element.click()
        # 点击确定
        self.find(By.XPATH, "//*[@text='确定']").click()
        # 跳转搜索界面
        return SearchPage(self.driver, self.dict_data)
