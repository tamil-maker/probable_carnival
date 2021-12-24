import unittest, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

 

def setUp():
    expected_value = 0
    desired_cap = {
                    'os_version': '10',
                    'os': 'Windows',
                    'browser': 'chrome',
                    'browser_version': 'latest',
                    'name': 'Parallel Test1', # test name
                    'build': 'browserstack-build-1', # Your tests will be organized within this build
                    'browserstack.debug': 'true'
                    }



    driver = webdriver.Remote(
    command_executor='https://tamilmaker_4IWx9K:kXpF5zHk3vsUvma57tZD@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap)
 
    
    "An example test:cansr login page and click login button"
    driver.get("https://www.cansrdev.com/clinical/dashboard/")


    time.sleep(6)
    if (driver.title=='Cansr | Login'):
        print("Sucess:Cansr login page sucessfully open")
        expected_value = expected_value + 1
    else:
        print("Failed:Cansr login page is not open")
    time.sleep(5)
setUp()        


"""
    def test_Cansr_Login(self):
        self.email= self.driver.find_element_by_xpath("//input[@id='inp_loginid']").send_keys("joercampell1@yopmail.com")
        self.password=self.driver.find_element_by_xpath("//input[@id='inp_password']").send_keys("Joe123!")
        time.sleep(6)
        self.login =self.driver.find_element_by_xpath("//button[text()='Login']").click()
        time.sleep(5)
        
        
if __name__ == '__main__':
    unittest.main()

obj=SeleniumOnBrowserStack(platform=options.platform,browserName=options.browserName,device=options.device)   
obj.setUp()
obj.run_session() 
obj.test_setup()
obj.test_Cansr_Login()

"""

