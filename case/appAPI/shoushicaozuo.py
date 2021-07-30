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
        el=self.driver.find_element_by_xpath("//*[@text='图文']")
        TouchAction(self.driver).tap(el).perform()
        el=self.driver.find_element_by_xpath("//*[@text='视频']")
        TouchAction(self.driver).press(el).release().perform()
        TouchAction(self.driver).long_press(x=500,y=500,duration=2000).release().perform()




