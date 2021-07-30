import os
import unittest
import time
from public.loginApp import Mylogin
from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['fullReset'] = 'True'
        desired_caps['app'] = PATH(r'E:\软件测试工作任务\zuiyou518.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    # def testshouye01_01(self):
    #     '''验证首页导航栏文案显示是否正常'''
    #     time.sleep(8)
    #     self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/home_item").click()
    #     time.sleep(6)
    #     navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
    #     self.assertEqual(navText[0].text,"关注")
    #     self.assertEqual(navText[1].text, "推荐")
    #     self.assertEqual(navText[2].text, "视频")
    #     self.assertEqual(navText[3].text, "图文")

    def test_dl(self):
        self.driver.implicitly_wait(40)
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()
        except:
            pass
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        # self.driver.swipe(600,1250,600,1250,100)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()


    def test_login(self):
        self.driver.implicitly_wait(60)
        try:
            self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvConfirmWithBg").click()
        except:
            pass
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/me_item").click()
        # self.driver.swipe(600,1250,600,1250,100)
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login_mode").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/phone_num_edit").send_keys("15127409611")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/code_edit").send_keys("a123456")
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/login").click()
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/textTabItem").click()
        navText = self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        self.assertEqual(navText[0].text, "关注")
        self.assertEqual(navText[1].text, "推荐")
        self.assertEqual(navText[2].text, "视频")
        self.assertEqual(navText[3].text, "图文")