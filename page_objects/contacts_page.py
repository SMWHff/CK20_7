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
from page_objects.manage_contact_page import ManageContact
from page_objects.search_page import SearchPage


class ContactsPage(BasePage):
    """
    通讯录界面类
    """
    _base_activity = ".launch.WwMainActivity"

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
        # 点击添加成员按钮
        self.find(By.XPATH, "//*[@text='添加成员']").click()
        return AddMemberPage(self.driver, self.dict_data)

    def goto_manage_contact(self):
        """
        跳转到管理通讯录
        :return: 返回管理通讯录界面类
        """
        # 获取通讯录总人数
        self.dict_data["count"] = self.get_member_count()
        # 点击左上角的管理设置按钮
        self.swipe_find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/top_bar_right_button2']").click()
        return ManageContact(self.driver, self.dict_data)

    def get_member_count(self):
        """
        获取通讯录总人数
        :return: 返回人数
        """
        # 判断当前页面列表人数是否 <= 1
        # 因为通讯录只有1个人的时候，不会显示人数
        locator = (By.XPATH, "//*[@resource-id='com.tencent.wework:id/contact_list']/android.widget.RelativeLayout")
        list_element = self.finds(locator)
        if len(list_element) <= 1:
            # 是就直接返回 1
            return 1
        else:
            # 滑动到底部，获取显示的总人数
            text = self.swipe_find(By.XPATH, "//*[contains(@text, '人未加入')]").text
            # 获取字符串切片开始索引
            start_index = text.find("共")
            # 获取字符串切片结束索引
            end_index = text.find("人")
            # 通过切片，获取中间的数字
            # 通过 int 将字符串转为数值
            count = int(text[start_index+1:end_index])
            # 返回总人数
            return count

    def is_exists(self, name=None):
        """
        判断指定成员是否存在通讯录中
        :return: 返回结果
        """
        # 判断 name 是否为空
        if name is None:
            # 为空则从 dict_data 字典中获取值
            name = self.dict_data['name']
        # 最多循环滑动5次
        for i in range(5):
            # 判断指定姓名是否存在列表中，存在则返回 True
            if len(self.find(By.XPATH, f"//*[@text='{name}']")) > 0:
                return True
            # 如果出现 ”人未加入“ 表示滑到底了还未找到，则返回 False
            if len(self.finds(By.XPATH, "//*[contains(@text, '人未加入')]")) > 0:
                return False
            # 打印运行日志
            self.log_info("没有找到，滑一下")
            # 向下滑动一页
            self.swipe()
        # 循环5次还未找到，则返回 False
        return False
