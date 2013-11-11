from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, random


class Griffith1Population(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    def test_griffith1_population(self, driver):
        driver = self.driver
    
    #_______________________________ Variables Set
        trackplace = random.randrange(1,150,1)
        genrepage = random.randrange(1,20,1)
        genre = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 37, 38, 39, 40, 41, 49]
        
        print "trackplace", (trackplace)
        print "genrepage", (genrepage)
        print "genre", (genre)
    #____________________________________________End Gathering Data_Begin Population/Login
        driver.get("https://accounts.beatportdev.com/login")
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
    #____________________________________________Setting up 5 random genres 
        for y in range(0,3):
            trackplace = random.randrange(1,150,1)
            genrepage = random.randrange(1,20,1)
            genre = random.randrange(4,18,1)
            print "trackplace", (trackplace)
            print "genrepage", (genrepage)
            print "genre", (genre)
            driver.get("http://sushi.beatportdev.com/genre/breaks/"+str(genre)+"/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page="+str(genrepage)+"") 
        #____________________________________________Setting up 100 random track purchases
            for x in range(0, 50):
                driver.find_element_by_xpath("//div[@id='body']/div/div[3]/table/tbody/tr["+str(trackplace)+"]/td[9]/a/span[2]").click()
                trackplace = random.randrange(1,150,1)
                print "We're on x time %d" % (x)
                print "We're on y time %d" % (y)
        
        self.driver.find_element_by_css_selector("span.count").click()
        driver.find_element_by_id("coupon-code-input").clear()
        driver.find_element_by_id("coupon-code-input").send_keys("test")
        driver.find_element_by_id("coupon-submit-btn").click()
        driver.find_element_by_css_selector("a.btn-submit.evtCheckout > span").click()
        driver.switch_to_frame("iframe-checkout")
        driver.find_element_by_id("cvv2").clear()
        driver.find_element_by_id("cvv2").send_keys("455")
        driver.find_element_by_css_selector("button.btn-submit.").click()
        driver.find_element_by_css_selector("span.my-bp-item.checkbox").click()
        driver.find_element_by_css_selector("button.btn-submit.").click()
        
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
        
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
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
