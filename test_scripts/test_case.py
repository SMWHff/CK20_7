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

@allure.feature("生成测试用例")
@pytest.fixture(scope="session")
def test_generate_case_date():
    """
    生成测试用例数据
    """
    Utils.generate_case_data()


@allure.feature("执行测试用例")
class TestCase:
    """
    执行测试用例
    """

    def setup_class(self):
        """
        在类开始之前执行初始化 appium，并启动 App
        """
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown_class(self):
        """
        仅类结束之后执行，关闭 App
        """
        self.app.stop()

    def teardown(self):
        """
        每个测试函数运行后执行一次返回操作
        """
        self.app.back()

    @pytest.mark.run(order=1)
    @allure.feature("测试添加成员")
    @allure.title("添加成员用例，姓名：{name}，手机：{phone}")
    @pytest.mark.parametrize("name,phone", Utils.get_case_data()[0], ids=Utils.get_case_data()[1])
    def test_addmember(self, name, phone):
        """
        添加成员测试用例
        1、进入到主界面
        2、在主界面点击通讯录按钮，进入到通讯录界面
        3、在通讯录界面点击➕添加成员按钮，进入到添加成员界面
        4、在添加成员界面点击手动输入添加按钮，进入到新建成员界面
        5、输入姓名、手机号，点击保存按钮，跳转回到添加成员界面
        6、查找 toast 提示框，并返回提示框内容
        """
        with allure.step("进入到主界面"):
            page = self.main
        with allure.step("在主界面点击通讯录按钮，进入到通讯录界面"):
            page = page.goto_contacts()
        with allure.step("在通讯录界面点击➕添加成员按钮，进入到添加成员界面"):
            page = page.goto_addmember()
        with allure.step("在添加成员界面点击手动输入添加按钮，进入到新建成员界面"):
            page = page.goto_addmember_by_manual()
        with allure.step("输入姓名、手机号，点击保存按钮，跳转回到通讯录界面"):
            page = page.new_member(name, phone)
        with allure.step("识别 toast 提示框，并返回提示框内容"):
            result = page.get_toast()
        assert result == "添加成功"

    # @pytest.mark.skip
    @pytest.mark.run(order=2)
    @allure.feature("测试删除成员")
    @allure.title("删除成员用例，姓名：{name}")
    @pytest.mark.parametrize("name", Utils.get_case_data()[2], ids=Utils.get_case_data()[3])
    def test_delmember(self, name):
        """
        删除成员测试用例
        1、进入到主界面
        2、在主界面点击通讯录按钮，进入到通讯录界面
        3、在通讯录界面点击搜索图标，进入到搜索界面
        4、在搜索界面输入姓名进行搜索，点击第一个搜索结果，进入到个人信息显示界面
        5、在个人信息显示界面点击右上角的三个点，进入到个人信息设置界面
        6、在个人信息设置界面点击编辑成员按钮，进入到编辑成员界面
        7、在编辑成员界面点击删除成员按钮，并点击确定按钮，跳转回到搜索界面
        8、在搜索界面再查找该姓名，并返回查找结果
        """
        with allure.step("进入到主界面"):
            page = self.main
        with allure.step("在主界面点击通讯录按钮，进入到通讯录界面"):
            page = page.goto_contacts()
        with allure.step("在通讯录界面点击搜索图标，进入到搜索界面"):
            page = page.goto_search()
        with allure.step("在搜索界面输入姓名进行搜索，点击第一个搜索结果，进入到个人信息显示界面"):
            page = page.search(name)
        with allure.step("在个人信息显示界面点击右上角的三个点，进入到个人信息设置界面"):
            page = page.goto_member_settings()
        with allure.step("在个人信息设置界面点击编辑成员按钮，进入到编辑成员界面"):
            page = page.goto_editmember()
        with allure.step("在编辑成员界面点击删除成员按钮，并点击确定按钮，跳转回到搜索界面"):
            page = page.del_member()
        with allure.step("在搜索界面再查找该姓名，并返回查找结果"):
            result = page.get_search_desc()
        assert "无搜索结果" in result
