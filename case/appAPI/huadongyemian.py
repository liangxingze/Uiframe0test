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
        self.driver.find_element_by_xpath("//*[@text='图文']").click()
        height=self.driver.get_window_size()['height']
        width=self.driver.get_window_size()['width']
        print('此手机的分辨率是：'+str(height)+'*'+str(width))

        self.driver.swipe(500,500,500,1000,2000)
        self.driver.swipe(500,500,500,500,100)
