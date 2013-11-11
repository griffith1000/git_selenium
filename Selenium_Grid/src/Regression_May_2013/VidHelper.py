        
'''
Created on April 11th, 2013


'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from castro import Castro 
import unittest, time, re, random

class VidHelper(unittest.TestCase):

    def setUp(self):
            self.screenCapture = Castro(filename="createprofile.swf")
            self.screenCapture.start()
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://stage-dj.beatport.com/"
            self.verificationErrors = []
            self.generateData()
       
        
        
    def addVideo(self):
        self.driver.find_element_by_link_text("Videos").click()
        self.driver.find_element_by_id("video_url").clear()
        self.driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=IzgFXpZsLYA&feature=plcp")
        self.driver.find_element_by_xpath("//input[@value='Add Video']").click()
        self.driver.find_element_by_id("video_url").click()
        self.driver.find_element_by_id("video_url").clear()
        self.driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=cHzhlJ48UjM&feature=plcp")
        self.driver.find_element_by_xpath("//input[@value='Add Video']").click()
        time.sleep(4)
    

        
        
    def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
    def tearDown(self):
            self.driver.quit()
            self.screenCapture.stop();
            self.assertEqual([], self.verificationErrors)

    def testFullRegression(self):
            self.registerDJ(self.djname, self.random1)
            self.createProfile(self.djname, self.random1, self.rndgenre1, self.rndgenre2, self.rndgenre3)






if __name__ == "__main__":
    unittest.main()
