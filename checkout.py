'''
Created on Jun 24, 2013

@author: ian.griffith
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random


class Griffith1Population(unittest.TestCase):
    def setUp(self):
        
        
        
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '7'
        desired_capabilities['platform'] = 'MAC'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

        #self.driver = webdriver.Firefox()
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
        
        
        self.driver = webdriver.Remote(
        desired_capabilities=desired_capabilities,
        command_executor="http://griffith10000:fca16075-e9c1-4531-84d0-e20e49282b9e@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_griffith1_population(self):
        driver = self.driver
    
        driver.get("https://stage-accounts.beatport.com/login")
        time.sleep(2)
        driver.find_element_by_id("username").clear()
        time.sleep(2)
        driver.find_element_by_id("username").send_keys("griffith1")
        time.sleep(2)
        driver.find_element_by_id("password").clear()
        time.sleep(2)
        driver.find_element_by_id("password").send_keys("beatport1")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        driver.get("http://stage-www.beatport.com/cart")
        time.sleep(2)
        driver.find_element_by_css_selector("a.btn-submit.evtCheckout > span").click()
        time.sleep(2)
        driver.switch_to_frame("iframe-checkout")
        time.sleep(2)
        driver.find_element_by_xpath("//input[@id=\"cvv2\"]").send_keys("324")
        time.sleep(2)
        #driver.find_element_by_id("cvv2").clear()
    #time.sleep(2)
        #driver.find_element_by_id("cvv2").send_keys("455")
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        #driver.find_element_by_css_selector("button.btn-submit.").click()
        time.sleep(35)
        #driver.find_element_by_css_selector("span.my-bp-item.checkbox").click()
    #time.sleep(2)
        #driver.find_element_by_css_selector("button.btn-submit.").click()


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
