'''
Created on Jun 24, 2013

@author: ian.griffith
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re, random


class Griffith1Population(unittest.TestCase):
    def setUp(self):
        
        self.driver = webdriver.Remote (
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities=DesiredCapabilities.CHROME)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
#        self.generateData()

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
