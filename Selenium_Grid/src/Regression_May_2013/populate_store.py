
'''
Created on April 11th, 2013


'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random


class DJHelpers(unittest.TestCase):
    

    def setUp(self):
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://stage-dj.beatport.com/"
            self.verificationErrors = []
            self.generateData()


    def generateData(self):
            self.bio = "   "
            self.driver = self.driver
            self.event = random.randrange(1,47000,1);   
            self.profile = random.randrange(1,150000,1);    
            self.random1 = random.randrange(2000,99999,1);
            self.photo = random.randrange(1,1043,1);
            self.photo2 = random.randrange(1,1043,1);
            self.photo5 = random.randrange(1,1043,1);
            self.rndgenre1 = random.randrange(1,23,1);
            self.rndgenre2 = random.randrange(1,23,1);
            self.rndgenre3 = random.randrange(1,23,1);
            self.rndgenre4 = random.randrange(1,23,1);
            self.rndgenre5 = random.randrange(1,23,1);
            self.rndgenre6 = random.randrange(1,23,1);
            self.dj1 = random.randrange(1,15,1);
            self.trackplace = random.randrange(1,150,1)
            self.genrepage = random.randrange(1,100,1)
            self.genre = random.randrange(1,26,1)
            
                
            print "dj1", str(self.dj1)
            print "random1", str(self.random1)
            print "event", str(self.event)
            print "photo", str(self.photo)
            print "photo2", str(self.photo2)
            print "photo 5", str(self.photo5)
            print "profile", str(self.profile)
            self.driver.get("http://dj.beatport.com/profile/" + str(self.profile))
            self.profile_url = self.driver.current_url
            print(self.profile_url)
            self.djname = self.driver.find_element_by_css_selector("h1").text
            self.bio = self.driver.find_element_by_id("bio").text
            print"djname", (self.djname)
            print "bio",(self.bio)
            
  


        #____________________________________________End Gathering Data__Begin registering
    def registerDJ(self, djname, random, trackplace, genre, genreplace):
            print "End Gathering Data__Begin registering"
            driver=self.driver
            driver.get("http://stage-dj.beatport.com/")
            time.sleep(3)
            driver.get("https://stage-accounts.beatport.com/register")
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
            #changed the submit button - was searching it by css-selector, i changed it to xpath
            driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        
    
            trackplace = random.randrange(1,150,1)
            genrepage = random.randrange(1,100,1)
            genre = random.randrange(1,26,1)
            
            print "trackplace", (trackplace)
            
        
            driver.get("http://stage-www.beatport.com/genre/breaks/${genre}/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page=${genrepage} http://stage-www.beatport.com/genre/house/9/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page=${genrepage}")
            driver.find_element_by_xpath("//div[@id='body']/div/div[3]/table/tbody/tr[${trackplace}]/td[9]/a/span[2]").click()
        
            driver.find_element_by_xpath("//div[@id='body']/div/div[3]/table/tbody/tr[${trackplace}]/td[9]/a/span[2]").click()
        
            driver.find_element_by_xpath("//div[@id='body']/div/div[3]/table/tbody/tr[${trackplace}]/td[9]/a/span[2]").click()
        
         
            driver.find_element_by_css_selector("span.count").click()
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
    
    def testFullRegression(self):
        self.registerDJ(self.djname, self.random1)
            

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
