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

    def test_element_by_id(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/title")
        print(el.text)
        el.click()

    def test_01(self):
        self.driver.implicitly_wait(60)
        el=self.driver.find_elements_by_id("cn.xiaochuankeji.tieba:id/title")
        print(el)
        el[3].click()

    def test_02(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@text='图文']").click()

    def test_03(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@text='图文']/../../../android.widget.FrameLayout[3]/android.widget.FrameLayout/android.widget.TextView").click()

    def test_0456789(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/search_b']/android.widget.ImageView").click()
        self.driver.find_element_by_xpath("//android.widget.EditText").send_keys('666')
        self.driver.find_element_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/search_input_clear']").click()
        self.driver.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/cancel" and @class="android.widget.TextView"]').click()
        el=self.driver.find_elements_by_xpath("//*[@resource-id='cn.xiaochuankeji.tieba:id/textTabItem']")
        el[3].click()
        self.driver.find_element_by_xpath('//*[@text="空间动态"]').click()

    def test_10(self):
        self.driver.implicitly_wait(60)
        el=self.driver.find_elements_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/iconTabItem"]')
        el[2].click()

    def test_11(self):
        self.driver.implicitly_wait(60)
        el = self.driver.find_elements_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/iconTabItem"]')
        el[1].click()

    def test_12(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/home_refresh_view"]').click()

    def test_131415(self):
        self.driver.implicitly_wait(60)
        self.driver.find_element_by_xpath('//*[@resource-id="cn.xiaochuankeji.tieba:id/holder_flow_rmdv"]').click()
        self.driver.find_element_by_xpath('//*[contains(@resource-id,"id/operate_share")]').click()
        self.driver.find_element_by_xpath('//*[@text="收藏"]').click()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
