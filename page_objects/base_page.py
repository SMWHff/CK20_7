# !/usr/bin python3
# -*- encoding: utf-8 -*-
# @Author     : SMWHff
# @Email      : SMWHff@163.com
# @IDE        : PyCharm
# @Project    : CK20_7
# @File       : base_page.py
# @Time       : 2021/9/12 19:40
import logging
import time
from typing import Dict
import allure
from tools.utils import Utils
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# 设置用例文件路径
case_yml = Utils.get_root_path() + "/data/case.yml"


class BasePage:
    """
    基础父类，用于其他类继承公共资源共享
    """
    _base_activity = ".launch.WwMainActivity"
    _save_filename = f"{Utils.get_root_path()}/data/{time.strftime('%Y-%m-%d %H-%M-%S')}.png"

    def __init__(self, base_driver: WebDriver = None, base_data: Dict = None):
        # 判断 dict_data 字典是否存在
        if base_data is None:
            self.dict_data = dict()
        else:
            self.dict_data = base_data
        # 判断 driver 对象是否存在
        if base_driver is None:
            # log输出日志界别
            logging.basicConfig(level=logging.DEBUG)
            # appium 连接配置
            caps = {
                "platformName": "Android",
                "platformVersion": "6.0.1",
                "deviceName": "网易模拟器",
                "automationName": "Appium",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                "newCommandTimeout": 300,
                "noReset": True
            }
            # 连接 appium server
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 设置隐式等待 3 秒
            self.driver.implicitly_wait(3)
        else:
            # 存在的话就赋值给当前实例类里
            self.driver = base_driver
        # 显示等待 30 秒内是否进入当前界面
        self.wait_until(self.driver, 30, lambda x: x.current_activity == self._base_activity)

    def find(self, by, value=None):
        """
        查找元素
        :param by: 查找方式
        :param value: 元素特征
        :return: 返回元素对象
        """
        for i in range(2):
            try:
                locator = by if value is None else (by, value)
                self.log_info(f"正在查找元素：{locator}")
                return self.driver.find_element(*locator)
            except NoSuchElementException:
                # 未找到元素，可能存在弹窗遮挡
                if i == 0:
                    # 进入弹窗处理流程
                    self.handling_popup()
        msg = "唉~ 找了好久，还是未找到元素！"
        self.log_info(msg)
        raise NoSuchElementException(msg)

    def finds(self, by, value=None):
        """
        查找所有符合条件的元素
        :param by: 查找方式
        :param value: 元素特征
        :return: 返回元素对象
        """
        if value is None:
            self.log_info(f"正在查找所有匹配元素：{by}")
            return self.driver.find_elements(*by)
        else:
            self.log_info(f"正在查找所有匹配元素：{(by,value)}")
            return self.driver.find_elements(by, value)

    def swipe_find(self, by, value, num=5):
        """
        向下滑动查找元素
        :param by:定位器类型
        :param value:定位器的值
        :param num:滑动次数上限
        :return:返回找到的元素
        """
        for i in range(num):
            try:
                self.log_info(f"正在滑动查找元素：{[by, value]}")
                element = self.driver.find_element(by, value)
                return element
            except NoSuchElementException:
                self.log_info("没有找到，滑一下")
                self.swipe()
        msg = f"唉！找了{num}次，还是没找到！"
        self.log_info(msg)
        raise NoSuchElementException(msg)

    def swipe(self):
        """
        向下滑动一页
        """
        # 获取屏幕大小
        size = self.driver.get_window_size()
        width = size.get("width")
        height = size.get("height")
        # 起点坐标
        start_x = width / 2
        start_y = height * 0.8
        # 终点坐标
        end_x = start_x
        end_y = height * 0.4
        # 滑动时长 2 秒
        duration = 2000
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def get_activity(self):
        """
        获取当前界面的 ACTIVITY
        :return: 返回ACTIVITY
        """
        return self.driver.current_activity

    def screenshot(self):
        """
        截取APP界面快照
        :return: 返回图片文件路径
        """
        self.driver.get_screenshot_as_file(self._save_filename)
        return self._save_filename

    @staticmethod
    def log_info(text):
        """
        打印日志信息
        """
        logging.info(text)

    def wait_until(self, driver, timeout, method):
        """
        显示等待条件成立
        :param driver: 驱动对象
        :param timeout: 超时秒数
        :param method: 条件方法
        :return: 返回结果
        """
        try:
            # 显示等待条件成立
            WebDriverWait(driver, timeout).until(method)
        except TimeoutException:
            # 显示等待超时，开始执行弹窗处理流程
            self.handling_popup()

    def wait_until_not(self, driver, timeout, method):
        """
        显示等待条件不成立
        :param driver: 驱动对象
        :param timeout: 超时秒数
        :param method: 条件方法
        :return: 返回结果
        """
        try:
            # 显示等待条件不成立
            WebDriverWait(driver, timeout).until_not(method)
        except TimeoutException:
            # 显示等待超时，开始执行弹窗处理流程
            self.handling_popup()

    def handling_popup(self):
        """
        处理随机弹窗
        :return: 返回处理结果
        """
        result = None
        # 存放各种弹窗界面的处理列表
        list_popups = [
            ["标题", "组件名", [("定位器类型", "定位器的值")]],
            ["标题", ".contact.controller.WorkMateRecommendActivity", [(By.XPATH, "//*[@text='跳过']")]],
            ["添加成员出错", ".contact.controller.ContactAddFastModeActivity", [(By.XPATH, "//*[@text='确定']"), (By.ID, "com.tencent.wework:id/top_bar_left_button1")]]
        ]
        # 获取当前界面的组件名
        cur_activity = self.get_activity()
        # 遍历弹窗列表库
        for popup in list_popups:
            # 标题
            popup_title = popup[0]
            # 组件名
            popup_activity = popup[1]
            # 定位器
            list_locator = popup[2]
            # 判断当前界面是否存在弹窗列表中
            if cur_activity == popup_activity:
                # 输出日志信息
                self.log_info(f"发现弹窗：{popup_title}")
                # 存在，则点击对应的按钮处理掉
                for popup_locator in list_locator:
                    self.log_info(f"正在处理弹窗：{popup_locator}")
                    self.driver.find_element(*popup_locator).click()
                # 成功返回元素
                result = True
        if not result:
            # 当前出现的弹窗未在弹窗列表库中
            self.log_info(f"【异常】当前界面：{cur_activity}")
            # 将截图贴到报告中
            allure.attach.file(self.screenshot(), "【异常】截图", attachment_type=allure.attachment_type.PNG)
            # 将界面布局源码贴到报告中
            allure.attach(self.driver.page_source, "【异常】布局源码", attachment_type=allure.attachment_type.XML)
        return result
