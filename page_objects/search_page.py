# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : search_page.py
# @Time       : 2021/9/16 17:55
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from page_objects.base_page import BasePage
from page_objects.member_info_page import MemberInfoPage


class SearchPage(BasePage):
    """
    搜索界面
    """
    _base_activity = ".contact.controller.DepartmentSearchActivity"

    def search(self, name):
        """
        搜索查找成员
        :return: 返回个人信息显示界面类
        """
        # 传递姓名给后面的类使用
        self.dict_data["name"] = name
        # 输入姓名
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/search_bar_text']").send_keys(name)
        # 点击找到的结果
        self.find(By.XPATH, f"//android.view.ViewGroup/*[@text='{name}']").click()
        return MemberInfoPage(self.driver, self.dict_data)

    def get_search_desc(self):
        """
        获取搜索结果提示
        :return: 返回提示内容
        """
        # 元素定位器
        locator = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/empty_view_desc']")
        # 强制等待 10 秒判断元素是否显示
        self.wait_until(self.driver, 10, expected_conditions.visibility_of_element_located(locator))
        # 获取搜索结果信息
        text = self.find(locator).text
        return text
