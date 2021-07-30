import os
import unittest
import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['noReset'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'
        desired_caps['automationName']='Uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        #self.driver.quit()
        pass


    def test_01(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/middle_view').click()
        self.driver.find_element_by_id('cn.xiaochuankeji.tieba:id/etInput').send_keys('666')
        self.driver.find_element_by_xpath('//*[@text="发送"]').click()
        toast_loc=('xpath',".//*[contains(@text,'评论发送成功')]")
        # le=self.driver.find_element_by_xpath("//*[contains(@text,'请先登录')]")
        el=WebDriverWait(self.driver,20,0.1).until(EC.presence_of_element_located(toast_loc))
        print(el)






