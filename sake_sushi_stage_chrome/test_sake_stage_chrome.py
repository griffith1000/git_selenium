
'''
Created on April 11th, 2013


'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest, time, re, random


class DJHelpers(unittest.TestCase):
    

    def setUp(self):
#            #self.driver = webdriver.Firefox()
            #self.driver = webdriver.Chrome
#            self.driver = webdriver.Chrome('/Users/ian.griffith/chromedriver')
#            #self.driver = webdriver.Firefox()
#            self.driver.implicitly_wait(30)
#            self.base_url = "http://stage-sake-dj.beatport.com/"
#            self.verificationErrors = []
#            self.generateData()

#self.driver = webdriver.Firefox()
            self.driver = webdriver.Chrome
            self.driver = webdriver.Chrome('/Users/ian.griffith/chromedriver')
#            self.driver = webdriver.Remote (
#            command_executor='http://localhost:4444/wd/hub',
#            desired_capabilities=DesiredCapabilities.CHROME)
#            #self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(30)
            self.base_url = "http://stage-sake-dj.beatport.com/"
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
            time.sleep(2)
            self.djname = self.driver.find_element_by_css_selector("h1").text
            self.bio = self.driver.find_element_by_id("bio").text
            print"djname", (self.djname)
            print "bio",(self.bio)
            
  


        #____________________________________________End Gathering Data__Begin registering
    def registerDJ(self, djname, random):
            print "End Gathering Data__Begin registering"
            driver=self.driver
            driver.get("http://stage-sake-dj.beatport.com/")
            #time.sleep(3)
            driver.get("https://stage-sake-accounts.beatport.com/register")
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
        
        #_____________________________________________End registering account__begin create djs profile
        
    def createProfile(self, djname, bio, random1, rndgenre1, rndgenre2, rndgenre3, rndgenre4, rndgenre5, rndgenre6):
            print "End registering account__begin create djs profile"
            time.sleep(2)
            driver=self.driver
            driver.get("http://stage-sake-dj.beatport.com/")
            driver.switch_to_default_content()
            time.sleep(2)
            driver.find_element_by_id("site-nav-item-Create Profile").click()
            time.sleep(2)
#            driver.find_element_by_xpath("//*[@id=\"header\"]/div/div[2]/ul/li[3]/a").click()   
            driver.find_element_by_id("profile_name").clear()
            driver.find_element_by_id("profile_name").send_keys(djname)
            driver.find_element_by_id("profile_slug").clear()
            driver.find_element_by_id("profile_slug").send_keys(djname + str(random1))
            driver.find_element_by_id("profile_bio").clear()
            driver.find_element_by_id("profile_bio").send_keys("dj" + str(random1) + " password beatport1 -------- " + self.bio)
            #driver.find_element_by_id("profile_image").send_keys("/home/ian.griffith/Desktop/numbered_djs/dj" + str(self.photo) + ".jpg")
            driver.find_element_by_id("profile_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(self.photo) + ".jpg")
            time.sleep(2)
#            driver.find_element_by_xpath("//input[@value='Create Profile']").click()
            time.sleep(5)
            #  ___end create dj profile___Begin genres
            print "end create dj profile___Begin genres"
            
#            driver.find_element_by_css_selector("#genre-list > li").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[2]").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[3]").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[4]").click()

            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre1) + "]").click()
            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre2) + "]").click()
            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre3) + "]").click()            
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre4) + "]").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre5) + "]").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre6) + "]").click()
#            driver.find_element_by_xpath("//ul[@id='genre-list']/li[" + str(rndgenre1) + "]").click()
            driver.find_element_by_id("profile-settings-submit").click()
#            driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre1) + "]").click()
#            driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre2) + "]").click()
#            driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre3) + "]").click()
#            driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre3) + "]").click()

#            time.sleep(2)
#            # __create dj profile____begin management
#            print "create dj profile____begin management"
#            driver.find_element_by_link_text("Management").click()
#            driver.find_element_by_name("username").clear()
#            driver.find_element_by_name("username").send_keys("griffith1")
#            driver.find_element_by_xpath("//input[@value='Add Manager']").click()
#
#
##  I split off the video as a test
#            print "end management begin video"
#            time.sleep(2)
#            self.driver.find_element_by_link_text("Videos").click()
#            self.driver.find_element_by_id("video_url").clear()
#            self.driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=IzgFXpZsLYA&feature=plcp")
#            self.driver.find_element_by_xpath("//input[@value='Add Video']").click()
#            
#    def addVideo(self):
#            driver=self.driver
#            driver.find_element_by_id("video_url").click()
#            driver.find_element_by_id("video_url").clear()
#            driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=cHzhlJ48UjM&feature=plcp")
#            driver.find_element_by_xpath("//input[@value='Add Video']").click()
#            time.sleep(4)
#            
#            
##___________create dj profile________begin Soundcloud add
#
#    def addSoundCloud(self): 
#            print "create dj profile________begin Soundcloud add"
#            self.driver.find_element_by_link_text("SoundCloud").click()
#            self.driver.find_element_by_link_text("Individual Tracks").click()
#            time.sleep(5)
#            self.driver.find_element_by_id("soundcloud_track_url").clear()
#            self.driver.find_element_by_id("soundcloud_track_url").send_keys("http://soundcloud.com/maisondragen/armin-van-buuren-we-are-here-to-make-some-noise-maison-dragen-remix-edit")
#            time.sleep(2)
#            self.driver.find_element_by_xpath("//input[@value='Add Track']").click()
#            time.sleep(2)
#            #...............  End Create DJ Profile begin search/follow/unfollow
#    def addSearchFollow(self): 
#            self.driver.get("http://stage-sake-dj.beatport.com/")
#            print "Create DJ Profile___ begin search/follow/unfollow"
##            self.driver.find_element_by_name("q").clear()
##            self.driver.find_element_by_name("q").send_keys("djrocket&space")
##            self.driver.find_element_by_css_selector("input.search-submit").click()
#            self.driver.get("http://stage-sake-dj.beatport.com/rocketmachine")  
#            self.driver.find_element_by_xpath("//div[@id='profile-index']/div[3]/a/img").click()
#            self.driver.find_element_by_xpath("//form[@id='profile-follow']/a/span").click()
#            self.driver.find_element_by_css_selector("a.btn").click()
#            self.driver.save_screenshot("/Users/ian.griffith/Desktop/automationscreenshots/main_page.png")
#            
#         
            #.................  End Follow/Unfollow/Search___ begin create chart
    def addChart(self, djname, photo2, random1, bio): 
            print "End Follow/Unfollow/Search___ begin create chart"
            self.driver.get("http://stage-sake-dj.beatport.com/")
            self.driver.find_element_by_css_selector("a.btn").click()
            self.driver.find_element_by_link_text("Create New Chart").click()
            self.driver.find_element_by_id("chart_name").clear()
            self.driver.find_element_by_id("chart_name").send_keys(self.djname + "'s Chart")
            self.driver.find_element_by_id("chart_description").clear()
            self.driver.find_element_by_id("chart_description").send_keys("dj" + str(self.random1) + " password beatport1 -------- " + self.bio + " ${biostage1}")
            #self.driver.find_element_by_id("chart_image").send_keys("/home/ian.griffith/Desktop/numbered_djs/dj" + str(self.photo2) + ".jpg")
            self.driver.find_element_by_id("chart_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(self.photo2) + ".jpg")
            self.driver.find_element_by_css_selector("input.btn.primary").click()
            time.sleep(6)
            self.driver.find_element_by_link_text("+ Add Tracks").click()
            self.driver.find_element_by_id("query").clear()
            self.driver.find_element_by_id("query").send_keys("happy")
            self.driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[3]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[4]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[5]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[6]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[7]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[8]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[9]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[11]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[10]").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("(//input[@value='Add Track'])[13]").click()
            time.sleep(6)
            self.driver.find_element_by_id("publish-chart-link").click()
            time.sleep(6)
            self.driver.find_element_by_css_selector("#publish-modal > div.modal-footer > form.nonAjax > input.btn.primary").click()
#_______________________End create Chart________Begin create event
    def addEvent(self, photo5, event):   
            print "End create Chart________Begin create event"
            self.driver.get("http://dj.beatport.com/events/" + str(self.event))
            Event_Title = self.driver.find_element_by_css_selector("h1").text
            self.driver.get("http://stage-sake-dj.beatport.com/")
            time.sleep(3)
            self.driver.find_element_by_css_selector("a.btn").click()
            self.driver.find_element_by_link_text("Create New Event").click()
            self.driver.find_element_by_id("event_title").clear()
            time.sleep(1)
            self.driver.find_element_by_id("event_title").send_keys(Event_Title)
            time.sleep(1)
            self.driver.find_element_by_id("event_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(self.photo5) + ".jpg")
            time.sleep(1)
            self.driver.find_element_by_id("event_description").click()
            time.sleep(1)
            self.driver.find_element_by_id("event_description").clear()
            time.sleep(1)
            self.driver.find_element_by_id("event_description").send_keys("dj" + str(self.random1) + " password beatport1 -------- " + str(self.bio))
            time.sleep(1)
            self.driver.find_element_by_css_selector("input.btn.primary").click()
            time.sleep(1)
            self.driver.find_element_by_id("venueName").click()
            self.driver.find_element_by_id("venueName").clear()
            self.driver.find_element_by_id("venueName").send_keys(self.djname + "'s Venue")
            self.driver.find_element_by_css_selector("input.btn.primary").click()
            self.driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").clear()
            self.driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("DJRocket&Space")
            self.driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
            time.sleep(4)
            self.driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
            time.sleep(4)
            self.driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").clear()
            time.sleep(4)
#            self.driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("invalyd")
#            self.driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
#            time.sleep(4)
#            self.driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
#            time.sleep(4)
#            self.driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("mcguyface")
#            self.driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
#            time.sleep(4)
#            self.driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
            self.driver.find_element_by_css_selector("span.drop-menu-prompt").click()
            self.driver.find_element_by_link_text("Log Out").click()



    def verifypaypal(self):
        driver=self.driver
        driver.get("http://stage-sake-dj.beatport.com/")
        driver.find_element_by_css_selector("a > span").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='body']/div/div/div[3]/ul/li[4]/div/div[2]/div/div[2]/div/a/span[3]/span").click()
##        driver.find_element_by_xpath("//div[@id='body']/div/div/div[3]/ul/li[2]/div/div[2]/div/div[2]/div/a/span[2]")click()
#        driver.find_element_by_css_selector("span.count").click()
#        driver.find_element_by_css_selector("a.btn-submit.evtCheckout > span").click()
#        driver.find_element_by_id("radio-pay-pal").click()
#        driver.find_element_by_id("billTo_street1").clear()
#        driver.find_element_by_id("billTo_street1").send_keys("ian street")
#        driver.find_element_by_id("billTo_city").clear()
#        driver.find_element_by_id("billTo_city").send_keys("chico")
#        driver.find_element_by_id("billTo_postalCode").clear()
#        driver.find_element_by_id("billTo_postalCode").send_keys("94107")
#        # ERROR: Caught exception [ReferenceError: selectLocator is not defined]
#
#        driver.find_element_by_css_selector("button.btn-submit.").click()
#        driver.find_element_by_link_text("Account Settings").click()
#        # Warning: verifyTextPresent may require manual changes
#        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*City\nchico[\\s\\S]*$")
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        # Warning: verifyTextPresent may require manual changes
#        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Postal Code\n94107[\\s\\S]*$")
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        # Warning: verifyTextPresent may require manual changes
#        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Card Type\nPayPal[\\s\\S]*$")
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        # Warning: verifyTextPresent may require manual changes
#        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, "^[\\s\\S]*Street Address\nian street[\\s\\S]*$")
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        driver.find_element_by_link_text("Log Out").click()


#
#            
#    def testFullRegression(self):
##           self.registerDJ(self.djname, self.random1)
#            self.verifypaypal
#      
            
            
    def testFullRegression(self):
            self.registerDJ(self.djname, self.random1)
            self.createProfile(self.djname, self.bio, self.random1, self.rndgenre1, self.rndgenre2, self.rndgenre3, self.rndgenre4, self.rndgenre5, self.rndgenre6)
#            self.addVideo()
#            self.addSoundCloud()
#            self.addSearchFollow()
            self.addChart(self.djname, self.photo2, self.random1, self.bio)
            self.addEvent(self.event, self.photo5)

            
    def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()
