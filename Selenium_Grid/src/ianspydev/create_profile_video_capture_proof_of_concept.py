from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from castro import Castro 
import time, unittest 

class create_profile (unittest.TestCase) :
    def setUp(self) :

        self.screenCapture = Castro(filename="testGoogleSearch.swf")
        self.screenCapture.start()
        self.driver = webdriver.Firefox()
        
    def testGoogleSearch(self) :
        driver = self.driver
        driver.get("http://www.google.com")
        inputElement = driver.find_element_by_name("q")
        inputElement.send_keys("Cheese!")
        inputElement.submit()
        WebDriverWait(driver, 20).until(lambda driver : driver.title.lower().startswith("cheese!"))
        self.assertEqual("cheese! - Google Search",driver.title)
    
    def tearDown(self) :
        self.driver.quit()
        # Stop the recording
        self.screenCapture.stop();
        
    if __name__ == "__main__":
        unittest.main()