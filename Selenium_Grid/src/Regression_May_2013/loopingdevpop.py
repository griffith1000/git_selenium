from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random

class Griffith1Population(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://stage-dj.beatport.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_griffith1_population(self):
     
        driver = webdriver.Firefox()
        trackplace = random.randrange(1,150,1)
        genrepage = random.randrange(1,100,1)
        genre = random.randrange(1,3,1)
        
     

        print "trackplace", (trackplace)
        print "genrepage", (genrepage)
        print "genre", (genre)
        #____________________________________________End Gathering Data__Begin registering
    

        driver.get("https://accounts.beatportdev.com/login")
        time.sleep(6)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("griffith1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("beatport1")
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()

    for x in range(0, 50):
            print x
        #driver.get("http://stage-www.beatport.com/genre/breaks/3/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page=1") 
        #driver.get("http://stage-www.beatport.com/genre/breaks/"+str(genre)+"/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page="+str(genrepage)+"") 

            trackplace = random.randrange(1,150,1)
            genrepage = random.randrange(1,100,1)
            genre = random.randrange(5,18,1)
            driver = self
    driver.get("http://sushi.beatportdev.com/genre/breaks/"+ str(x) +"/tracks?perPage=150&sortBy=publishDate+DESC%2C+releaseId+DESC&page="+str(genrepage)+"") 


    for y in range(0, 50):
            trackplace = random.randrange(1,150,1)
            genrepage = random.randrange(1,100,1)
            genre = random.randrange(5,18,1)

            print y
            driver.find_element_by_xpath("//div[@id='body']/div/div[3]/table/tbody/tr["+str(trackplace)+"]/td[9]/a/span[2]").click()
            trackplace = random.randrange(1,150,1)

            print "We're on y time %d" % (y)
            print "We're on x time %d" % (x)

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException : return False
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