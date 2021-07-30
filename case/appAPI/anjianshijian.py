import os
import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #self.driver.quit()
        pass

    def test_01(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView").click()
        self.driver.find_element_by_xpath("//android.widget.EditText").send_keys('666')
        self.driver.keyevent(67)
        self.driver.keyevent(66)
        self.driver.keyevent(4)
