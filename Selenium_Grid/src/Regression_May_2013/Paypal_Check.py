from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random

class PayPalCheck(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def verifypaypal(self, self.profile, self.random1):
    
        driver = self.driver
        self.profile = random.randrange(1,150000,1);
        self.random1 = random.randrange(2000,10000,1);
        driver.get("http://dj.beatport.com/self.profile/" + str(self.profile))
        profile_url = driver.current_url
        print(profile_url)
        djname = driver.find_element_by_css_selector("h1").text
        print(djname)
        driver.find_element_by_id("bp-btn-register").click()
        driver.switch_to_frame("form-frame")
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys(djname)
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys(djname)
        driver.find_element_by_id("emailAddress").clear()
        driver.find_element_by_id("emailAddress").send_keys("ian.griffith+" + str(self.random1) +"@beatport.com")
        driver.find_element_by_id("confirmEmailAddress").clear()
        driver.find_element_by_id("confirmEmailAddress").send_keys("ian.griffith+" + str(self.random1) +"@beatport.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dj" + str(self.random1))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("beatport1")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("beatport1")
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(10)
        
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_css_selector("a > span").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='body']/div/div/div[3]/ul/li[4]/div/div[2]/div/div[2]/div/a/span[3]/span").click()
#        driver.find_element_by_xpath("//div[@id='body']/div/div/div[3]/ul/li[2]/div/div[2]/div/div[2]/div/a/span[2]")click()
        driver.find_element_by_css_selector("span.count").click()
        driver.find_element_by_css_selector("a.btn-submit.evtCheckout > span").click()
        driver.find_element_by_id("radio-pay-pal").click()
        driver.find_element_by_id("billTo_street1").clear()
        driver.find_element_by_id("billTo_street1").send_keys("ian street")
        driver.find_element_by_id("billTo_city").clear()
        driver.find_element_by_id("billTo_city").send_keys("chico")
        driver.find_element_by_id("billTo_postalCode").clear()
        driver.find_element_by_id("billTo_postalCode").send_keys("94107")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]

        driver.find_element_by_css_selector("button.btn-submit.").click()
        driver.find_element_by_link_text("Account Settings").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*City\nchico[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Postal Code\n94107[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Card Type\nPayPal[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Street Address\nian street[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text("Log Out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
#    def is_alert_present(self):
#        try: self.driver.switch_to_alert()
#        except NoAlertPresentException, e: return False
#        return True


    def testFullRegression(self):
        self.verifypaypal(self, self.profile, self.random1)
    
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

