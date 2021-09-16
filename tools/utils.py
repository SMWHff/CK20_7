# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7_1
# @File       : utils.py
# @Time       : 2021/9/13 8:41
import yaml
from faker import Faker
from conftest import case_yml


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
    def generate_case_data(cls, num=10):
        """
        随机生成测试用例数据，并保存到 yml 文件
        :return: 返回 yml 文件路径
        """
        faker = Faker("zh_CN")
        case_data = {
            "add_member": {
                "data": [],
                "ids": []
            },
            "del_member": {
                "data": [],
                "ids": []
            }
        }
        for i in range(num):
            name = faker.name()
            phone = faker.phone_number()
            case_data["add_member"]["data"].append([name, phone])
            case_data["add_member"]["ids"].append(f"添加{name}")
            case_data["del_member"]["data"].append(name)
            case_data["del_member"]["ids"].append(f"删除{name}")
        with open(case_yml, "w", encoding="utf-8") as f:
            yaml.dump(case_data, f)
        return case_yml

    @classmethod
    def get_case_data(cls):
        """
        从 yml 文件中加载测试用例数据
        :return: 返回测试用例数据
        """
        with open(case_yml, encoding="utf-8") as f:
            case_data = yaml.safe_load(f)
        add_member_data = case_data.get("add_member").get("data")
        add_member_ids = case_data.get("add_member").get("ids")
        del_member_data = case_data.get("del_member").get("data")
        del_member_ids = case_data.get("del_member").get("ids")
        # add_member_fail_data = case_data.get("add_member_fail").get("data")
        # add_member_fail_ids = case_data.get("add_member_fail").get("ids")
        return \
            add_member_data, add_member_ids, \
            del_member_data, del_member_ids # , \
            # add_member_fail_data, add_member_fail_ids


if __name__ == "__main__":
    print(Utils.generate_case_data())
