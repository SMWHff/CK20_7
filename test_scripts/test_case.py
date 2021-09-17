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

_base_app = None

def start_app():
    """
    启动APP
    :return: 返回App对象
    """
    # 全局定义 _base_app 对象
    global _base_app
    # 判断 _base_app 对象是否存在
    if _base_app is None:
        # 不存在就实例化一个
        _base_app = App()
    # 返回 _base_app 对象
    return _base_app

@pytest.fixture(scope='class')
@allure.title("前置步骤")
def class_fixture_addmember():
    """
    用于实现 test_addmember 的专属 setup_class、teardown_class
    :return: (app对象,page对象)
    """
    # 启动APP
    app = App()
    # 第一步
    with allure.step("1.进入到主界面"):
        page = app.start().goto_main()
    # 第二步
    with allure.step("2.在主界面点击通讯录按钮，进入到通讯录界面"):
        page = page.goto_contacts()
    # 第三步
    with allure.step("3.在通讯录界面点击➕添加成员按钮，进入到添加成员界面"):
        page = page.goto_addmember()
    # yield 之前实现的是 setup_class 功能
    yield page
    # yield 之后实现的是 teardown_class 功能
    # 关闭APP
    # app.stop()


@pytest.fixture(scope='class')
@allure.title("前置步骤")
def class_fixture_addmember_fail():
    """
    用于实现 test_addmember_fail 的专属 setup_class、teardown_class
    :return: (app对象,page对象)
    """
    # 启动APP
    app = App()
    # 第一步
    with allure.step("1.进入到主界面"):
        page = app.start().goto_main()
    # 第二步
    with allure.step("2.在主界面点击通讯录按钮，进入到通讯录界面"):
        page = page.goto_contacts()
    # 第三步
    with allure.step("3.在通讯录界面点击➕添加成员按钮，进入到添加成员界面"):
        page = page.goto_addmember()
    # 第四步
    with allure.step("4.在添加成员界面点击手动输入添加按钮，进入到新建成员界面"):
        page = page.goto_addmember_by_manual()
    # yield 之前实现的是 setup_class 功能
    yield page
    # yield 之后实现的是 setup_class 功能
    # 关闭APP
    # app.stop()


@pytest.fixture(scope='class')
@allure.title("前置步骤")
def class_fixture_delmember():
    """
    用于实现 test_delmember 的专属 setup_class、teardown_class
    :return: (app对象,page对象)
    """
    # 启动App
    app = App()
    # 第一步
    with allure.step("1.进入到主界面"):
        page = app.start().goto_main()
    # 第二步
    with allure.step("2.在主界面点击通讯录按钮，进入到通讯录界面"):
        page = page.goto_contacts()
    # 第三步
    with allure.step("3.在通讯录界面点击搜索图标，进入到搜索界面"):
        page = page.goto_search()
    # yield 之前实现的是 setup_class 功能
    yield page
    # yield 之后实现的是 setup_class 功能
    # 关闭APP
    # app.stop()



@allure.feature("执行测试用例")
class TestCase:
    """
    执行测试用例
    """

    # @pytest.mark.skip
    # @pytest.mark.run(order=1)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("测试添加成员成功")
    @allure.title("添加成员成功用例，姓名：{name}，手机：{phone}")
    @pytest.mark.parametrize("name,phone", Utils.get_case_data()[0], ids=Utils.get_case_data()[1])
    def test_addmember(self, name, phone, class_fixture_addmember):
        """
        添加成员成功测试用例
        1、进入到主界面
        2、在主界面点击通讯录按钮，进入到通讯录界面
        3、在通讯录界面点击➕添加成员按钮，进入到添加成员界面
        4、在添加成员界面点击手动输入添加按钮，进入到新建成员界面
        5、输入姓名、手机号，点击保存按钮，跳转回到添加成员界面
        6、查找 toast 提示框，并返回提示框内容
        """
        # 第四步
        with allure.step("4.在添加成员界面点击手动输入添加按钮，进入到新建成员界面"):
            page = class_fixture_addmember[0].goto_addmember_by_manual()
        # 第五步
        with allure.step("5.输入姓名、手机号，点击保存按钮，跳转回到通讯录界面"):
            page = page.new_member(name, phone)
        # 第六步
        with allure.step("6.识别 toast 提示框，并返回提示框内容"):
            result = page.get_toast()
        # 将截图贴到报告中
        allure.attach.file(page.screenshot(), "截图", attachment_type=allure.attachment_type.PNG)
        assert result == "添加成功"

    # @pytest.mark.skip
    # @pytest.mark.run(order=2)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("测试添加成员失败")
    @allure.title("添加成员失败用例，姓名：{name}，手机：{phone}，预期：{expect}")
    @pytest.mark.parametrize("name,phone,expect", Utils.get_case_data()[4], ids=Utils.get_case_data()[5])
    def test_addmember_fail(self, name, phone, expect, class_fixture_addmember_fail):
        """
        添加成员失败测试用例
        1、进入到主界面
        2、在主界面点击通讯录按钮，进入到通讯录界面
        3、在通讯录界面点击➕添加成员按钮，进入到添加成员界面
        4、在添加成员界面点击手动输入添加按钮，进入到新建成员界面
        5、输入姓名、手机号，点击保存按钮，并返回提示内容
        """
        # 第五步
        with allure.step("5.输入姓名、手机号，点击保存按钮，并返回提示内容"):
            result = class_fixture_addmember_fail[0].new_member_fail(name, phone)
        # 将截图贴到报告中
        allure.attach.file(class_fixture_addmember_fail[0].screenshot(), "截图", attachment_type=allure.attachment_type.PNG)
        assert result == expect

    # @pytest.mark.skip
    # @pytest.mark.run(order=3)
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("测试删除成员成功")
    @allure.title("删除成员成功用例，姓名：{name}")
    @pytest.mark.parametrize("name", Utils.get_case_data()[2], ids=Utils.get_case_data()[3])
    def test_delmember(self, name, class_fixture_delmember):
        """
        删除成员成功测试用例
        1、进入到主界面
        2、在主界面点击通讯录按钮，进入到通讯录界面
        3、在通讯录界面点击搜索图标，进入到搜索界面
        4、在搜索界面输入姓名进行搜索，点击第一个搜索结果，进入到个人信息显示界面
        5、在个人信息显示界面点击右上角的三个点，进入到个人信息设置界面
        6、在个人信息设置界面点击编辑成员按钮，进入到编辑成员界面
        7、在编辑成员界面点击删除成员按钮，并点击确定按钮，跳转回到搜索界面
        8、在搜索界面再查找该姓名，并返回查找结果
        """
        # 第四步
        with allure.step("4.在搜索界面输入姓名进行搜索，点击第一个搜索结果，进入到个人信息显示界面"):
            page = class_fixture_delmember[0].search(name)
        # 第五步
        with allure.step("5.在个人信息显示界面点击右上角的三个点，进入到个人信息设置界面"):
            page = page.goto_member_settings()
        # 第六步
        with allure.step("6.在个人信息设置界面点击编辑成员按钮，进入到编辑成员界面"):
            page = page.goto_editmember()
        # 第七步
        with allure.step("7.在编辑成员界面点击删除成员按钮，并点击确定按钮，跳转回到搜索界面"):
            page = page.del_member()
        # 第八步
        with allure.step("8.在搜索界面再查找该姓名，并返回查找结果"):
            result = page.get_search_desc()
        # 将截图贴到报告中
        allure.attach.file(page.screenshot(), "截图", attachment_type=allure.attachment_type.PNG)
        assert "无搜索结果" == result
