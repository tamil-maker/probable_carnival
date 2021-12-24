
import time
from selenium import webdriver
# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

#driver get method is navigate a page given by a URL
driver.get("https://weathershopper.pythonanywhere.com/")

curtemp=driver.find_element_by_xpath("//span[@id='temperature']")

# Text method is used to read the object value
curtemp = curtemp.text
# Split method used to split the strings into list
split_string=curtemp.split()
# Using the slicing operation and getting the value and converting into int
my_value = int(split_string[-2])

if my_value<= 19 :
    weather=driver.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]")
    weather.click()
    time.sleep(2)

elif my_value>=34:
    #buy sunscreen xpath://button[contains(text(),'Buy sunscreens')]
    weather=driver.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
    weather.click()
else:
    print("The temperature is between 19 and 34. So no need to click any button")
    
