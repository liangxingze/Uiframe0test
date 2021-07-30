# coding=utf-8
from selenium import webdriver
import unittest
import os
import time
from public.login import Mylogin

class Gouwuche(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.2.249:8080")
        self.driver.maximize_window()
        time.sleep(5)

    def tearDown(self):
        filedir = "D:/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('D:/', 'test', 'screenshot'))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()


    def testcrm13_01(self):
        '''跟进次数排行页面'''
        Mylogin(self.driver).login()

        Shouye=self.driver.find_element_by_xpath("//*[text()='跟进次数排行（按拜访时间统计）']")
        self.assertEqual('跟进次数排行（按拜访时间统计）',Shouye.text)

    def testcrm13_02(self):
        '''时间框-下拉选择'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[7]').click()

        crmSjkText = self.driver.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[1]/span/div/input').get_attribute("value")

        print(crmSjkText)

        self.assertEqual("本季度",crmSjkText)



    def testcrm13_03(self):
        '''时间框-自定义起始时间框页面'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath("//*[@aria-label='后一年']").is_displayed())

    def testcrm13_04(self):
        '''时间框-自定义起始时间框正常选择时间'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='el-date-table']/tbody/tr[5]/td[3]/div/span").click()
        time.sleep(2)
        crmCssj=self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").get_attribute("value")

        self.assertEqual("2021-07-20",crmCssj)

    def testcrm13_05(self):
        '''自定义-起始时间框“《”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='前一年']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_06(self):
        '''自定义-起始时间框“<”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='上个月']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")

        self.assertNotEqual(a,crmQnTest.text)

    def testcrm13_07(self):
        '''自定义-起始时间框“》”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='后一年']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_08(self):
        '''自定义-起始时间框“>”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='下个月']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_09(self):
        '''时间框-自定义终止时间框页面'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
        self.assertTrue(self.driver.find_element_by_xpath("//*[@aria-label='后一年']").is_displayed())


    def testcrm13_10(self):
        '''时间框-自定义终止时间框正常选择时间'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='el-date-table']/tbody/tr[5]/td[3]/div/span").click()
        time.sleep(2)
        crmCssj = self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").get_attribute("value")

        self.assertEqual("2021-07-20", crmCssj)


    def testcrm13_11(self):
        '''自定义-终止时间框“《”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='前一年']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_12(self):
        '''自定义-终止时间框“<”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='上个月']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")

        self.assertNotEqual(a,crmQnTest.text)

    def testcrm13_13(self):
        '''自定义-终止时间框“》”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='后一年']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[1]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_14(self):
        '''自定义-终止时间框“>”键'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        time.sleep(2)
        crmNfTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")
        a=print(crmNfTest.text)
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@aria-label='下个月']").click()
        time.sleep(2)
        crmQnTest=self.driver.find_element_by_xpath("//div[@class='el-date-picker__header']/span[2]")

        self.assertNotEqual(a,crmQnTest.text)


    def testcrm13_15(self):
        '''时间框-自定义时间'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[11]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[1]/input").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//table[@class='el-date-table']/tbody/tr[5]/td[3]/div/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").send_keys('2021-07-20')
        # self.driver.find_element_by_xpath("//*[@x-placement='bottom']/div[1]/div[2]/div[2]/input").click()
        # time.sleep(2)
        # self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[5]/td[3]/div/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//span[text()='确定']").click()
        time.sleep(2)
        crmSjkText = self.driver.find_element_by_xpath('//*[@id="crm-main-container"]/div/div/div[1]/span/div/input').get_attribute("value")

        print(crmSjkText)

        self.assertEqual("2021-07-20-2021-07-20",crmSjkText)



    def testcrm13_16(self):
        '''选择部门'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@placeholder='选择部门']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='财务部']").click()

        crmSjkText = self.driver.find_element_by_xpath("//*[@placeholder='选择部门']").get_attribute("value")

        print(crmSjkText)

        self.assertEqual("财务部",crmSjkText)


    def testcrm13_17(self):
        '''搜索'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("//*[@id='crm-main-container']/div/div/div[1]/span/div/input").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@x-placement="bottom"]/div[1]/div/div[7]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@placeholder='选择部门']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='财务部']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[text()='搜索']").click()
        time.sleep(2)

        self.assertTrue(self.driver.find_element_by_xpath("//*[text()='暂无排行']").is_displayed())






if __name__ == "__main__":
    unittest.main()



