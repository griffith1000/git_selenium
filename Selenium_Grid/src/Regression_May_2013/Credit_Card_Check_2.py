from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random

class CreditCardCheck2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_credit_card_check2(self):
        driver = self.driver
        profile = random.randrange(1,150000,1);
        random1 = random.randrange(2000,10000,1);
        driver.get("http://dj.beatport.com/profile/" + str(profile))
        profile_url = driver.current_url
        print(profile_url)
        djname = driver.find_element_by_css_selector("h1").text
        print(djname)
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_id("bp-btn-register").click()
        #added this line below because
        driver.switch_to_frame("form-frame")
        driver.find_element_by_id("first-name").clear()
        driver.find_element_by_id("first-name").send_keys(djname)
        driver.find_element_by_id("last-name").clear()
        driver.find_element_by_id("last-name").send_keys(djname)
        driver.find_element_by_id("emailAddress").clear()
        driver.find_element_by_id("emailAddress").send_keys("ian.griffith+" + str(random1) +"@beatport.com")
        driver.find_element_by_id("confirmEmailAddress").clear()
        driver.find_element_by_id("confirmEmailAddress").send_keys("ian.griffith+" + str(random1) +"@beatport.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dj" + str(random1))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("beatport1")
        driver.find_element_by_id("confirmPassword").clear()
        driver.find_element_by_id("confirmPassword").send_keys("beatport1")
        #changed the submit button - was searching it by css-selector, i changed it to xpath
        driver.find_element_by_css_selector("button.btn-submit.").click()
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_css_selector("a > span").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.find_element_by_xpath("//div[@id='body']/div/div/div[3]/ul/li[4]/div/div[2]/div/div[2]/div/a/span[3]/span").click()
        driver.find_element_by_css_selector("span.count").click()
        driver.find_element_by_css_selector("a.btn-submit.evtCheckout > span").click()
        driver.find_element_by_id("billTo_firstName").clear()
        driver.find_element_by_id("billTo_firstName").send_keys("ian")
        driver.find_element_by_id("billTo_lastName").clear()
        driver.find_element_by_id("billTo_lastName").send_keys("griffith")
        driver.find_element_by_id("card_accountNumber").clear()
        driver.find_element_by_id("card_accountNumber").send_keys("4111111111111111")
        driver.find_element_by_id("card_expirationMonth").clear()
        driver.find_element_by_id("card_expirationMonth").send_keys("12")
        driver.find_element_by_id("card_expirationYear").clear()
        driver.find_element_by_id("card_expirationYear").send_keys("2013")
        driver.find_element_by_id("billTo_street1").clear()
        driver.find_element_by_id("billTo_street1").send_keys("ian street")
        driver.find_element_by_id("billTo_city").clear()
        driver.find_element_by_id("billTo_city").send_keys("chico")
        driver.find_element_by_id("billTo_postalCode").clear()
        driver.find_element_by_id("billTo_postalCode").send_keys("94107")
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
        driver.find_element_by_css_selector("button.btn-submit.").click()
        driver.find_element_by_id("cvv2").clear()
        driver.find_element_by_id("cvv2").send_keys("455")
        driver.find_element_by_css_selector("button.btn-submit.").click()
        driver.find_element_by_link_text("Account Settings").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*City\nchico[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Postal Code\n94107[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Street Address\nian street[\\s\\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("span.drop-arrow").click()
        driver.find_element_by_link_text("Log Out").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
#   def is_alert_present(self):
#       try: self.driver.switch_to_alert()
#       except NoAlertPresentException, e: return False
#       return True
    
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
