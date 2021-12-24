import time
from selenium import webdriver
#create of instance Chrome driver
driver = webdriver.Chrome()
#driver get method is navigate a page given by a URL
driver.get("https://www.cansrdev.com/clinical/dashboard/")
#check if the title of the page is proper
if (driver.title=="Cansr|login"):
    print("Sucess:Cansr login page sucessfully open")
else:
    print("Failed:Cansr login page is not open")
time.sleep(2) 

#find the new user signup button using the path sign up//a[contains(text(),'Sign Up')]
sign_up = driver.find_element_by_xpath("//a[contains(text(),'Sign Up')]")
sign_up.click()

#firstname path //input[@id='inp_firstName']
first_name = driver.find_element_by_xpath("//input[@id='inp_firstName']")
#KEY POINT using send key method
first_name.send_keys('madisan')
time.sleep(2)

#find the lastname xpath://*[@id="inp_LastName"]
last_name=driver.find_element_by_xpath("//input[@id='inp_LastName']")
#KEY POINT using send key method
last_name.send_keys('quinn')
time.sleep(1)

#find the emailid xpath://input[@id='email']
email=driver.find_element_by_xpath("//input[@id='email']") 
#KEY POINT using send key method
email.send_keys('madisan123@yopmail.com')

#post code/zip code field using the path://*[@id="postcode"]
post_code=driver.find_element_by_xpath("//input[@id='postcode']")
#KEY POINT using send key method
post_code.send_keys('LE14')

#dropdown button xpath://select[@id='dobDate']
dobdate=driver.find_element_by_xpath("//select[@id='dobDate']")
#KEY POINT using send key method
dobdate.send_keys('14')

#find the month dropdown button xpath://select[@id='dobMonth']
month = driver.find_element_by_xpath("//select[@id='dobMonth']")  
#KEY POINT using send key method
month.send_keys('December')

#find the year dropdown button xpath://select[@id='dobYear']
year = driver.find_element_by_xpath("//select[@id='dobYear']")  
#KEY POINT using send key method
year.send_keys('1990')
time.sleep(4)

#enter the captha code path://label[@id='mainCaptcha']
cap_code=driver.find_element_by_xpath("//label[@id='mainCaptcha']")
cap_code.send_keys('sWih')
time.sleep(5)

#onclick xpath://input[@id='signup-consent']
onclick = driver.find_element_by_xpath("//input[@id='signup-consent']")
#KEY POINT using send key method
onclick.click()
time.sleep(4)

#find the submit button xpath://button[@id='SignupBut_signup']
submit=driver.find_element_by_xpath("//button[@id='SignupBut_signup']")
#KEY POINT using send key method
submit.click()
time.sleep(5)











