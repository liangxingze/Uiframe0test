import time


import random



class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver


    def longin(self):
        '''正常登录'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('com.wuye:id/phone').clear()
        self.driver.find_element_by_id('com.wuye:id/phone').send_keys('17732137626')
        self.driver.find_element_by_id('com.wuye:id/password').clear()
        self.driver.find_element_by_id('com.wuye:id/password').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/login_btn').click()

    def longinYg(self):
        ''' 工作人员正常登录'''
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_id('com.wuye:id/yuangong_login').click()
        self.driver.find_element_by_id('com.wuye:id/phone').clear()
        self.driver.find_element_by_id('com.wuye:id/phone').send_keys('17732137627')
        self.driver.find_element_by_id('com.wuye:id/password').clear()
        self.driver.find_element_by_id('com.wuye:id/password').send_keys('123456')
        self.driver.find_element_by_id('com.wuye:id/login_btn').click()




