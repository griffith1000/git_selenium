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

class one_profile (unittest.TestCase):
    def setUp(self):
        
        self.screenCapture = Castro(filename="createprofile.swf")
        self.screenCapture.start()
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
    
    def test_python_webdriver_unittest_full_regression(self):
        bio = "   "
        driver = self.driver
        event = random.randrange(1,47000,1);   
        profile = random.randrange(1,150000,1);    
        random1 = random.randrange(2000,10000,1);
        photo = random.randrange(1,1043,1);
        photo2 = random.randrange(1,1043,1);
        photo5 = random.randrange(1,1043,1);
        rndgenre1 = random.randrange(1,23,1);
        rndgenre2 = random.randrange(1,23,1);
        rndgenre3 = random.randrange(1,23,1);
        rndgenre4 = random.randrange(1,23,1);
        rndgenre5 = random.randrange(1,23,1);
        rndgenre6 = random.randrange(1,23,1);
        dj1 = random.randrange(1,15,1);
        
        print dj1
        print random1
        print event
        print photo
        print photo2
        print photo5
        print profile
        driver.get("http://dj.beatport.com/profile/" + str(profile))
        profile_url = driver.current_url
        print(profile_url)
        djname = driver.find_element_by_css_selector("h1").text
        print(djname)
        #____________________________________________End Gathering Data__Begin registering
        driver.get("http://stage-dj.beatport.com/")
        time.sleep(3)
        driver.get("https://stage-accounts.beatport.com/register")
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
        #switching back to home page after registration in next 2 lines
        #_____________________________________________End registering account__begin create dj profile
        time.sleep(3)
        driver.get("http://stage-dj.beatport.com/")
        driver.switch_to_default_content()
        driver.find_element_by_id("logo").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id=\"header\"]/div/div[2]/ul/li[3]/a").click()   
        
        driver.find_element_by_id("profile_name").clear()
        driver.find_element_by_id("profile_name").send_keys(djname)
        driver.find_element_by_id("profile_slug").clear()
        driver.find_element_by_id("profile_slug").send_keys("djname" + str(random1))
        driver.find_element_by_id("profile_bio").clear()
        driver.find_element_by_id("profile_bio").send_keys("dj" + str(random1) + " password beatport1 -------- " + bio)
        driver.find_element_by_id("profile_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(photo) + ".jpg")
        driver.find_element_by_xpath("//input[@value='Create Profile']").click()
        time.sleep(4)
        #  ___create dj profile___Begin genres
        driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre1) + "]").click()
        driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre2) + "]").click()
        driver.find_element_by_xpath("//div[@id='genre-list']/ul/li[" + str(rndgenre3) + "]").click()
        time.sleep(4)
        # __create dj profile____begin management
        driver.find_element_by_link_text("Management").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("griffith1")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("merrix")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("sillyhat")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("seanbo333")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("blissriot")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("paula")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("prldd")
        driver.find_element_by_xpath("//input[@value='Add Manager']").click()
        #__________create dj profile______begin video add
        driver.find_element_by_link_text("Videos").click()
        driver.find_element_by_id("video_url").clear()
        driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=IzgFXpZsLYA&feature=plcp")
        driver.find_element_by_xpath("//input[@value='Add Video']").click()
        driver.find_element_by_id("video_url").click()
        driver.find_element_by_id("video_url").clear()
        driver.find_element_by_id("video_url").send_keys("http://www.youtube.com/watch?v=cHzhlJ48UjM&feature=plcp")
        driver.find_element_by_xpath("//input[@value='Add Video']").click()
        time.sleep(4)
        #___________create dj profile________begin Soundcloud add
        driver.find_element_by_link_text("SoundCloud").click()
        driver.find_element_by_link_text("Individual Tracks").click()
        driver.find_element_by_id("soundcloud_track_url").clear()
        driver.find_element_by_id("soundcloud_track_url").send_keys("http://soundcloud.com/maisondragen/armin-van-buuren-we-are-here-to-make-some-noise-maison-dragen-remix-edit")
        driver.find_element_by_xpath("//input[@value='Add Track']").click()
        #...............  End Create DJ Profile___ begin search/follow/unfollow
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("djrocket&space")
        driver.find_element_by_css_selector("input.search-submit").click()
        driver.find_element_by_xpath("//div[@id='profile-index']/div[3]/a/img").click()
        driver.find_element_by_xpath("//form[@id='profile-follow']/a/span").click()
        driver.find_element_by_css_selector("a.btn").click()
        driver.save_screenshot("/Users/ian.griffith/Desktop/automationscreenshots/main_page.png")
        #.................  End Follow/Unfollow/Search___ begin create chart
        driver.find_element_by_link_text("Create New Chart").click()
        driver.find_element_by_id("chart_name").clear()
        driver.find_element_by_id("chart_name").send_keys(djname + "'s Chart")
        driver.find_element_by_id("chart_description").clear()
        driver.find_element_by_id("chart_description").send_keys("dj" + str(random1) + " password beatport1 -------- " + bio + " ${biostage1}")
        driver.find_element_by_id("chart_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(photo2) + ".jpg")
        driver.find_element_by_css_selector("input.btn.primary").click()
        driver.find_element_by_link_text("+ Add Tracks").click()
        driver.find_element_by_id("term").clear()
        driver.find_element_by_id("term").send_keys("happy")
        driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[3]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[4]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[5]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[6]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[7]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[8]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[9]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[11]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[10]").click()
        driver.find_element_by_xpath("(//input[@value='Add Track'])[13]").click()
        time.sleep(6)
        driver.find_element_by_id("publish-chart-link").click()
        time.sleep(6)
        #_______________________End create Chart________Begin create event
        driver.find_element_by_css_selector("#publish-modal > div.modal-footer > form.nonAjax > input.btn.primary").click()
        driver.get("http://dj.beatport.com/events/" + str(event))
        Event_Title = driver.find_element_by_css_selector("h1").text
        driver.get("http://stage-dj.beatport.com/")
        driver.find_element_by_css_selector("a.btn").click()
        driver.find_element_by_link_text("Create New Event").click()
        driver.find_element_by_id("event_title").clear()
        driver.find_element_by_id("event_title").send_keys(Event_Title)
        driver.find_element_by_id("event_image").send_keys("/Users/ian.griffith/Desktop/numbered_djs/dj" + str(photo5) + ".jpg")
        driver.find_element_by_id("event_description").click()
        driver.find_element_by_id("event_description").clear()
        driver.find_element_by_id("event_description").send_keys("dj" + str(random1) + " password beatport1 -------- " + str(bio) + " ${biostage1}")
        driver.find_element_by_css_selector("input.btn.primary").click()
        driver.find_element_by_id("venueName").click()
        driver.find_element_by_id("venueName").clear()
        driver.find_element_by_id("venueName").send_keys(djname + "'s Venue")
        driver.find_element_by_css_selector("input.btn.primary").click()
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").clear()
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("DJRocket&Space")
        driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
        time.sleep(4)
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").clear()
        time.sleep(4)
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("Nick Doyle")
        driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
        time.sleep(4)
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("invalyd")
        driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
        time.sleep(4)
        driver.find_element_by_css_selector("#dj-search > input[name=\"q\"]").send_keys("mcguyface")
        
        driver.find_element_by_xpath("(//input[@value='Search'])[2]").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[@id='profile-index']/div[2]/a/img").click()
        driver.find_element_by_css_selector("span.drop-menu-prompt").click()
                #  End create Event
        driver.find_element_by_link_text("Log Out").click()
        print("")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.screenCapture.stop();
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()



    