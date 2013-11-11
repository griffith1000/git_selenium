from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Iphonedemo3(unittest.TestCase):
    def setUp(self):
        
        self.driver = webdriver.Remote("http://10.12.4.159:3001/wd/hub", webdriver.DesiredCapabilities.IPHONE)
        #self.driver = IPhoneDriver("http://192.168.1.100:3001/wd/hub");
        #self.driver = IPhoneDriver("http://10.12.4.157:3001/wd/hub");
        #driver = webdriver.Remote("http://10.12.4.157:3001/wd/hub", webdriver.DesiredCapabilities.IPHONE)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-www.beatport.com/sake/style-guide"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_iphonedemo3(self):
        driver = self.driver
        driver.get("http://stage-www.beatport.com/sake/style-guide")
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/a/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div/div/div/a/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[2]/div/div[2]/div/ul/li/ul/li/ul/li/div/div/span[2]/a").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[3]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div/div/a[2]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[4]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[5]/div/div/a[2]").click()
        driver.find_element_by_xpath("//div[@id='content']/div[5]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[6]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[6]/div/div/a[2]/i").click()
        driver.find_element_by_xpath("//div[@id='content']/div[7]/div/table/tbody/tr/td/span/a/i").click()
        driver.find_element_by_id("google-geocomplete-location").clear()
        driver.find_element_by_id("google-geocomplete-location").send_keys("san francisco")
        driver.get("http://stage-www.beatport.com")
        driver.find_element_by_xpath("//div[@id='site-nav']/nav/ul/li[2]/a/span").click()
        driver.find_element_by_xpath("//div[@id='site-nav']/nav/ul/li[3]/a/span").click()
        driver.find_element_by_xpath("//div[@id='site-nav']/nav/ul/li[4]/a/span").click()
        driver.find_element_by_xpath("//div[@id='site-nav']/nav/ul/li[5]/a/span").click()
        driver.find_element_by_xpath("//div[@id='site-nav']/nav/ul/li[6]/a/span").click()
        driver.get("http://stage-www.beatport.com")
        driver.find_element_by_css_selector("a > span").click()
        driver.find_element_by_link_text("Breaks").click()
        driver.find_element_by_link_text("Drum & Bass").click()
        driver.find_element_by_link_text("Dubstep").click()
        driver.find_element_by_link_text("Electro House").click()
        driver.find_element_by_link_text("Electronica").click()
        driver.get("http://stage-www.beatport.com")
            
    def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()
