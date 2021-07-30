import os
import unittest
import time
from public.wuyemaoyan import Mylogin
from appium import webdriver
from public.suijishengcheng import PhoneNOGenerator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

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
        desired_caps['app'] = PATH(r'E:\软件测试工作任务\app-debug100.apk')
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['appPackage'] = 'com.wuye'
        desired_caps['appActivity'] = '.yonghu.LoginActivity'
        desired_caps['automationName']='Uiautomator2'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        filedir = "D:/test/APPtu/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'APPtu'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)


        self.driver.quit()



    def testwuyemaoyan5306(self):
        '''手机号-输入首位不为1的11位数字'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('com.wuye:id/go_register').click()
        self.driver.find_element_by_id('com.wuye:id/phone').clear()
        pg=PhoneNOGenerator()
        zh=pg.phoneNORandomGenerator()
        self.driver.find_element_by_id('com.wuye:id/phone').send_keys(zh)
        self.driver.find_element_by_id('com.wuye:id/password').clear()
        self.driver.find_element_by_id('com.wuye:id/password').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/password_again').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/name').send_keys('梁非凡')
        self.driver.find_element_by_id('com.wuye:id/address').send_keys('大唐不夜城ya')
        self.driver.find_element_by_id('com.wuye:id/regist_btn').click()
        el=self.driver.find_element_by_xpath('//*[@text="退出登录"]')
        self.assertTrue(el.is_displayed())


    def testwuyemaoyan5325(self):
        '''正常登录'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('com.wuye:id/phone').clear()
        self.driver.find_element_by_id('com.wuye:id/phone').send_keys('17732137626')
        self.driver.find_element_by_id('com.wuye:id/password').clear()
        self.driver.find_element_by_id('com.wuye:id/password').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/login_btn').click()
        el=self.driver.find_element_by_xpath('//*[@text="退出登录"]')
        self.assertTrue(el.is_displayed())

    def testwuyemaoyan5337(self):
        ''' 正常修改员工地址'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longin()
        self.driver.find_element_by_xpath('//*[@text="修改地址"]').click()
        self.driver.find_element_by_id('com.wuye:id/address').clear()
        pg=PhoneNOGenerator()
        zh=pg.phoneNORandomGenerator()
        self.driver.find_element_by_id('com.wuye:id/address').send_keys(zh)
        self.driver.find_element_by_id('com.wuye:id/button').click()
        el=self.driver.find_element_by_id('com.wuye:id/address')
        self.assertEqual(str(zh),el.text)

    def testwuyemaoyan5346(self):
        ''' 正常服务预约'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longin()
        self.driver.find_element_by_xpath('//*[@text="服务预约"]').click()
        pg=PhoneNOGenerator()
        zh=pg.phoneNORandomGenerator()
        self.driver.find_element_by_id('com.wuye:id/content').send_keys(zh)
        sj=time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        self.driver.find_element_by_id('com.wuye:id/time').send_keys(sj)
        self.driver.find_element_by_id('com.wuye:id/leixingRoot').click()
        self.driver.find_element_by_xpath('//*[@text="维修服务"]').click()
        self.driver.find_element_by_id('com.wuye:id/button').click()
        toast_loc = ('xpath', ".//*[contains(@text,'提交成功')]")
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        self.assertTrue(el)


    def testwuyemaoyan5348(self):
        ''' 我的订单页面'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longin()
        self.driver.find_element_by_xpath('//*[@text="我的订单"]').click()
        q=self.driver.find_element_by_xpath('//*[@text="我的报修"]')
        w=self.driver.find_element_by_xpath('//*[@text="待接单"]')
        e=self.driver.find_element_by_xpath('//*[@text="已接单"]')
        r=self.driver.find_element_by_xpath('//*[@text="待支付"]')
        a=self.driver.find_element_by_xpath('//*[@text="待评价"]')
        s=self.driver.find_element_by_xpath('//*[@text="已完成"]')
        self.assertEqual("我的报修",q.text)
        self.assertEqual("待接单",w.text)
        self.assertEqual("已接单",e.text)
        self.assertEqual("待支付",r.text)
        self.assertEqual("待评价",a.text)
        self.assertEqual("已完成",s.text)

    def testwuyemaoyan5350(self):
        ''' 待接单显示'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longin()
        self.driver.find_element_by_xpath('//*[@text="我的订单"]').click()
        el=self.driver.find_element_by_id('com.wuye:id/tv_type')
        self.assertEqual("待接单",el.text)


    def testwuyemaoyan5399(self):
        ''' 工作人员正常登录'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('com.wuye:id/yuangong_login').click()
        self.driver.find_element_by_id('com.wuye:id/phone').clear()
        self.driver.find_element_by_id('com.wuye:id/phone').send_keys('17732137627')
        self.driver.find_element_by_id('com.wuye:id/password').clear()
        self.driver.find_element_by_id('com.wuye:id/password').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/login_btn').click()
        el=self.driver.find_element_by_xpath('//*[@text="修改员工地址"]')
        self.assertEqual('修改员工地址',el.text)


    def testwuyemaoyan5410(self):
        ''' 正常抢单'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longinYg()
        self.driver.find_element_by_id('com.wuye:id/baoxiu').click()
        Jine=PhoneNOGenerator().six()
        self.driver.find_element_by_id('com.wuye:id/tv_price').send_keys(Jine)
        self.driver.find_element_by_id('com.wuye:id/qiangdan').click()
        self.driver.find_element_by_id('android:id/button1').click()
        toast_loc = ('xpath', ".//*[contains(@text,'抢单成功')]")
        el = WebDriverWait(self.driver, 20, 0.1).until(EC.presence_of_element_located(toast_loc))
        self.assertTrue(el)


    def testwuyemaoyan5352(self):
        ''' 已接单页面'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longin()
        self.driver.find_element_by_xpath('//*[@text="我的订单"]').click()
        self.driver.find_element_by_xpath('//*[@text="已接单"]').click()
        el=self.driver.find_element_by_id('com.wuye:id/tv_type')
        self.assertEqual("已接单待上门",el.text)



    def testwuyemaoyan5427(self):
        ''' 我的抢单页面'''
        self.driver.implicitly_wait(60)
        Mylogin(self.driver).longinYg()
        self.driver.find_element_by_xpath('//*[@text="我的抢单"]').click()
        q=self.driver.find_element_by_xpath('//*[@text="我的报修"]')
        w=self.driver.find_element_by_xpath('//*[@text="待接单"]')
        e=self.driver.find_element_by_xpath('//*[@text="已接单"]')
        r=self.driver.find_element_by_xpath('//*[@text="待支付"]')
        a=self.driver.find_element_by_xpath('//*[@text="待评价"]')
        s=self.driver.find_element_by_xpath('//*[@text="已完成"]')
        self.assertEqual("我的报修",q.text)
        self.assertEqual("待接单",w.text)
        self.assertEqual("已接单",e.text)
        self.assertEqual("待支付",r.text)
        self.assertEqual("待评价",a.text)
        self.assertEqual("已完成",s.text)







if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
