# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : __init__.py
# @Time       : 2021/9/12 19:41

import pytest
if __name__ == "__main__":
    # 启动测试用例，并清除旧报告，生成新的报告
    pytest.main(["-vs", "--alluredir", "./temp", "--clean-alluredir"])
    # 终端上输入 allure generate ./temp -o ./report --clean
