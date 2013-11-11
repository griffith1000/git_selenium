from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, random



class DJHelpers(unittest.TestCase):
    
    def setUp(self) :
#        WebDriver driver = new RemoteWebDriver(new URL("http://localhost:4444/wd/hub"), capability);
         self.driver = webdriver.Remote(
         command_executor='http://localhost:4444/wd/hub',
#        desired_capabilities=DesiredCapabilities.FIREFOX)
         desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)
#        self.driver = webdriver.Firefox()
#        self.driver.implicitly_wait(30)
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
    def registerDJ(self, djname, random):
            print "End Gathering Data__Begin registering"
            driver=self.driver
            driver.get("http://stage-dj.beatport.com/")
            time.sleep(3)
            driver.get("https://stage-accounts.beatport.com/register")
       



#            
#    def testFullRegression(self):
##           self.registerDJ(self.djname, self.random1)
#            self.verifypaypal
#      
            
            
    def testFullRegression(self):
            self.registerDJ(self.djname, self.random1)
        

            
    def is_element_present(self, how, what):
            try: self.driver.find_element(by=how, value=what)
            except NoSuchElementException, e: return False
            return True
        
    def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    unittest.main()




