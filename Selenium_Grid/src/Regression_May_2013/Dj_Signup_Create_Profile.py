'''
Created on Apr 11, 2013

@author: ian.griffith
'''
'''
Created on April 11th, 2013


'''

#from DjXpaths import DjXpaths
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random

class Gold_March_6th_regression (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
    
    def test_python_webdriver_unittest_full_regression(self):
        
        driver = self.driver
        profile = random.randrange(1,150000,1);
        random1 = random.randrange(2000,10000,1);
        photo = random.randrange(1,1043,1);
        #=======================================================================
        # event = random.randrange(1,47000,1);
       
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
        # # print random1
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
        
        
        #This is the creation of the dj profile
        
        driver.find_element_by_xpath("//div[@class='navigation']//li[3]/a").click()  
        #driver.find_element_by_xpath("id('header')/x:div/x:div[2]/x:ul/x:li[3]/x:a").click() 
        driver.find_element_by_id("profile_name").clear()
        driver.find_element_by_id("profile_name").send_keys(djname)
        driver.find_element_by_id("profile_slug").clear()
        driver.find_element_by_id("profile_slug").send_keys("djname" + str(random1))
        driver.find_element_by_id("profile_bio").clear()
        driver.find_element_by_id("profile_bio").send_keys("dj" + str(random1) + " password beatport1 -------- " + bio)
        #driver.find_element_by_id("profile_image").clear()
        driver.find_element_by_id("profile_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(photo) + ".jpg")
        driver.find_element_by_xpath("//input[@value='Create Profile']").click()