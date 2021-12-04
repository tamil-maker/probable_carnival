import time
from selenium import webdriver
#create of instance Chrome driver
driver = webdriver.Chrome()
#driver get method is navigate a page given by a URL
driver.get("https://www.cansrdev.com/clinical/dashboard/")

#find the email field using the xpath        
email = driver.find_element_by_xpath("//input[@id='inp_loginid']")
#KEY POINT:using send key method
email.send_keys('joercampell1@yopmail.com')

#Find the password field using xpath
password = driver.find_element_by_xpath ("//input[@id='inp_password']")
#KEY POINT:using send key method
password.send_keys("Joe123!")
time.sleep(2)

#find xpath for login //button[contains(text(),'Login')]
login = driver.find_element_by_xpath("//button[text()='Login']")
login.click()
time.sleep(5)

#click here to continue xpath://u[contains(text(),'Click here to continue')]
click_con = driver.find_element_by_xpath("//u[contains(text(),'Click here to continue')]")
click_con.click()
time.sleep(3)
driver.close()





