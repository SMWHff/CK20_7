# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : conftest.py
# @Time       : 2021/9/12 19:39

import time
import pytest
from typing import List


# 将Unicode码替换成文字
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    # 遍历所有的用例
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 日志文件按时间命名，自动生成
@pytest.fixture(scope="session", autouse=True)
def manage_logs(request):
    """Set log file name same as test name"""
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    root_dir = request.config.rootdir
    log_name = f"{root_dir}\log\\{now}.logs"
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
