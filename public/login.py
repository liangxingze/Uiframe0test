import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Mylogin(object):
    def __init__(self, driver):
        self.driver = driver

    def login(self):

        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[4]/div/button").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[text()='商业智能']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/div[2]/div/img').click()
        # self.driver.find_element_by_xpath("//span[text()='员工客户分析']").click()
        time.sleep(2)

        # self.driver.find_element_by_xpath("//span[text()='排行榜']")
        a=self.driver.find_element_by_xpath("//span[text()='排行榜']")
        ActionChains(self.driver).move_to_element(a).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/ul/a[7]/li").click()
        time.sleep(2)

    def logintwo(self):
        self.driver.find_element_by_name("username").send_keys("admin")
        self.driver.find_element_by_name("password").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@id='app']/div/div[2]/form/div[4]/div/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[text()='商业智能']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="app"]/section/section/aside/div/div[2]/div/img').click()
        time.sleep(2)
        a=self.driver.find_element_by_xpath("//span[text()='排行榜']")
        ActionChains(self.driver).move_to_element(a).perform()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[2]/ul/a[8]/li").click()
        time.sleep(2)

            


            
    