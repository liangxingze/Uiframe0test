import os
import unittest
import time
from appium import webdriver


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
        yemianmingzi=self.driver.current_activity
        print(yemianmingzi)
        el=self.driver.find_element_by_xpath('//*[@text="关注"]')
        print(el.get_attribute('className'))
        print(el.get_attribute('resourceId'))
        print(el.is_enabled())  #是否可用

