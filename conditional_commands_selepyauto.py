from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
driver.get("https://www.cansrdev.com/clinical/dashboard/")

user_ele=driver.find_element_by_name("username")

print(user_ele.is_displayed())  #return true/false based of element status
print(user_ele.is_enabled())  #return true/false 

pwd_ele=driver.find_element_by_name("password")

print(pwd_ele.is_displayed())  #return true/false based of element status
print(pwd_ele.is_enabled())  #return true/false 

user_ele.send_keys("madisan123@yopmail.com")
pwd_ele.send_keys("Madisan123!")

time.sleep(6)
driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()

