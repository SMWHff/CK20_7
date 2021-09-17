# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : utils.py
# @Time       : 2021/9/13 8:41
import os
import yaml
from faker import Faker


class Utils:
    """
    实用工具类
    """

    @classmethod
    def get_name(cls):
        """
        随机生成假的姓名数据
        :return: 返回姓名
        """
        return Faker("zh_CN").name()

    @classmethod
    def get_phone(cls):
        """
        随机生成假的手机号
        :return: 返回手机号
        """
        return Faker("zh_CN").phone_number()

    @classmethod
    def get_root_path(cls):
        """
        获取项目根目录的绝对路径
        :return: 返回项目根目录路径
        """
        root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        # 替换斜杠
        return root_path.replace("\\", "/")

    @classmethod
    def generate_case_data(cls, num=10):
        """
        随机生成测试用例数据，并保存到 yml 文件
        :return: 返回 yml 文件路径
        """
        from page_objects.base_page import case_yml
        case_data = {
            "add_member": {
                "data": [],
                "ids": []
            },
            "del_member": {
                "data": [],
                "ids": []
            },
            "add_member_fail": {
                "data": [
                    ["", None, "姓名不能为空"],
                    [" ", None, "姓名不能为空"],
                    [None, "", "手机号不能为空"],
                    [None, " ", "手机号不能为空"],
                    [None, "$", "请填写合法的手机号"],
                    [None, "1301234567", "请填写合法的手机号"],
                    [None, "01301234567", "请填写合法的手机号"]
                ],
                "ids": [
                    "姓名不能为空 <姓名留空>",
                    "姓名不能为空 <姓名为空格>",
                    "手机号不能为空 <手机留空>",
                    "手机号不能为空 <手机为空格>",
                    "请填写合法的手机号 <手机为$>",
                    "请填写合法的手机号 <手机号为10位>",
                    "请填写合法的手机号 <手机号为零开头11位>"
                ]
            }
        }
        for i in range(num):
            name = Utils.get_name()
            phone = Utils.get_phone()
            case_data["add_member"]["data"].append([name, phone])
            case_data["add_member"]["ids"].append(f"添加成功 <{name}>")
            case_data["del_member"]["data"].append(name)
            case_data["del_member"]["ids"].append(f"删除成功 <{name}>")
            if i == num - 1:
                case_data["add_member_fail"]["data"].append([name, phone, "手机已存在于通讯录，无法添加"])
                case_data["add_member_fail"]["ids"].append("手机已存在于通讯录，无法添加")
        length = len(case_data["add_member_fail"]["data"])
        for i in range(length):
            if case_data["add_member_fail"]["data"][i][0] is None:
                case_data["add_member_fail"]["data"][i][0] = Utils.get_name()
            if case_data["add_member_fail"]["data"][i][1] is None:
                case_data["add_member_fail"]["data"][i][1] = Utils.get_phone()
        with open(case_yml, "w", encoding="utf-8") as f:
            yaml.safe_dump(case_data, f, allow_unicode=True)
        return case_yml

    @classmethod
    def get_case_data(cls):
        """
        从 yml 文件中加载测试用例数据
        :return: 返回测试用例数据
        """
        from page_objects.base_page import case_yml
        yml_path = case_yml
        # 判断 case_yml 文件是否存在
        if not os.path.isfile(yml_path):
            # 随机生成测试用例数据并保存到 yml 文件
            yml_path = cls.generate_case_data()
        # 读取测试用例
        with open(yml_path, encoding="utf-8") as f:
            case_data = yaml.safe_load(f)
        add_member_data = case_data.get("add_member").get("data")
        add_member_ids = case_data.get("add_member").get("ids")
        del_member_data = case_data.get("del_member").get("data")
        del_member_ids = case_data.get("del_member").get("ids")
        add_member_fail_data = case_data.get("add_member_fail").get("data")
        add_member_fail_ids = case_data.get("add_member_fail").get("ids")
        return \
            add_member_data, add_member_ids, \
            del_member_data, del_member_ids, \
            add_member_fail_data, add_member_fail_ids


if __name__ == "__main__":
    print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    print(Utils.get_case_data())
