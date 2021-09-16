# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : test_case.py
# @Time       : 2021/9/12 19:40
import allure
import pytest
from page_objects.app import App
from tools.utils import Utils


class TestCase:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()


    def test_addmember(self):
        for name in ["何亮", "田丹", "谢桂芝", "张三", "李四", "王五", "赵六"]:
            # name = Utils.get_name()
            phone = Utils.get_phone()
            result = self.main \
                .goto_contacts() \
                .goto_addmember() \
                .goto_addmember_by_manual() \
                .new_member(name, phone) \
                .get_toast()
            assert result == "添加成功"
            self.app.back()

    def test_delmember(self):
        for name in ["田丹", "谢桂芝", "张三", "李四", "王五", "赵六"]:
            result = self.main \
                .goto_contacts() \
                .goto_search() \
                .search(name) \
                .goto_member_settings() \
                .goto_editmember() \
                .del_member() \
                .get_search_desc()
            print(result)
            assert "无搜索结果" in result
            self.app.back()
