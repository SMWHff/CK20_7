# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : manage_contact_page.py
# @Time       : 2021/9/13 16:31
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from page_objects.member_edit_page import EditMemberPage


class ManageContact(BasePage):
    """
    管理通讯录界面类
    """
    _base_activity = ".contact.controller.EnterpriseContactActivity"

    def goto_editmember(self, name):
        """
        编辑指定成员
        :param name:
        :return:返回编辑成员界面类
        """
        # 传递姓名给后面的类使用
        self.dict_data["name"] = name
        # 点击编辑成员
        self.find(By.XPATH, f"//*[@text='{name}']").click()
        # 传递返回页面给后面的类使用
        self.dict_data["back_page"] = "ManageContact"
        # 跳转到编辑成员界面
        return EditMemberPage(self.driver, self.dict_data)

    def goto_contacts(self):
        """
        跳转到通讯录界面
        :return: 返回通讯录界面类
        """
        from page_objects.contacts_page import ContactsPage
        # 判断人数是否减少
        WebDriverWait(self, 30).until(lambda x: x.get_member_count() != x.dict_data.get("count"))
        # 删除前后人数对比
        self.log_info(f"删除前共{self.dict_data.get('count')} --> 删除后共{self.get_member_count()}人")
        # 点击通讯录按钮
        self.find(By.XPATH, "//*[@resource-id='com.tencent.wework:id/top_bar_right_button1']").click()
        return ContactsPage(self.driver, self.dict_data)

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
            count = int(text[start_index + 1:end_index])
            # 返回总人数
            return count


if __name__ == "__main__":
    from page_objects.app import App
    print("count：", App().start().goto_main().goto_contacts().goto_manage_contact().get_member_count())
