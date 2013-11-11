'''
Created on Apr 11, 2013

@author: ian.griffith
'''
'''
Created on April 11th, 2013


'''
from selenium import webdriver
        # from selenium.webdriver.common.by import By
        # from selenium.webdriver.support.ui import Select
        # from selenium.common.exceptions import NoSuchElementException
        # import time, re

import unittest, random



class Gold_March_6th_regression (unittest.TestCase):
    
    
    def setUp(self):
        self.driver = webdriver.Remote("http://localhost:3001/wd/hub", webdriver.DesiredCapabilities.IPHONE)
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
    
    def test_python_webdriver_unittest_full_regression(self):
        
        driver = self.driver
        profile = random.randrange(1,150000,1);
        random1 = random.randrange(2000,10000,1);
   
        #=======================================================================
        # event = random.randrange(1,47000,1);
        # photo = random.randrange(1,1043,1);
        # photo2 = random.randrange(1,1043,1);   
        # photo5 = random.randrange(1,1043,1);     
        # rndgenre1 = random.randrange(1,23,1);
        # rndgenre2 = random.randrange(1,23,1);
        # rndgenre3 = random.randrange(1,23,1);
        # rndgenre4 = random.randrange(1,23,1);
        # rndgenre5 = random.randrange(1,23,1);   
        # rndgenre6 = random.randrange(1,23,1);     
        # dj1 = random.randrange(1,15,1);
        # # print dj1
        print random1
        # # print event
        # # print photo
        # # print photo2
        # # print photo5
        # # print profile
        # # print rndgenre1
        # # print rndgenre2
        # # print rndgenre3
        # # print rndgenre4
        # # print rndgenre5
        # # print rndgenre6
        #=======================================================================

        
        
        
        driver.get("http://dj.beatport.com/profile/" + str(profile))
        profile_url = driver.current_url
        print(profile_url)
        djname = driver.find_element_by_css_selector("h1").text
        bio = driver.find_element_by_id("bio").text
        print(djname)
        print(bio)
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_id("btn-register").click()
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
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        #driver.get("http://stage-dj.beatport.com/")
        #switching back to home page after registration in next 2 lines
        driver.switch_to_default_content()
        driver.find_element_by_id("logo").click()