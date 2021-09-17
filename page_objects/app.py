# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : app.py
# @Time       : 2021/9/12 19:40
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from page_objects.main_page import MainPage


class App(BasePage):
    """
    APP操作类
    """
    _base_activity = ".launch.WwMainActivity"

    def start(self):
        """
        启动APP
        :return: 返回自身类
        """
        self.driver.launch_app()
        return self

    def stop(self):
        """
        关闭APP
        """
        self.driver.close_app()

    def restart(self):
        """
        重启APP
        :return: 返回自身类
        """
        self.stop()
        return self.start()

    def back(self):
        """
        后退操作
        """
        self.driver.back()

    def goto_main(self):
        """
        跳转到APP入口界面
        :return: 返回主界面类
        """
        # 设置显示等待 60 秒
        self.wait_until(self, 60, lambda x: len(x.finds(By.XPATH, "//*[@text='通讯录']")) > 0)
        return MainPage(self.driver)
