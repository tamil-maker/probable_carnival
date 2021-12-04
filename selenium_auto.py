# Create an instance of Firefox WebDriver
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
driver.get("https://www.cansrdev.com/clinical/dashboard/")

# Check if the title of the page is proper
if(driver.title=="Qxf2 Services: Selenium training main"):
    print ("Success: Qxf2 Tutorial page launched successfully")
else:
    print ("Failure: Qxf2 Tutorial page Title is incorrect")    

# Find the name field using xpath with id
name = driver.find_element_by_xpath("//input[@id='name']")
# KEY POINT: Send text to an element using send_keys method
name.send_keys('Avinash')

# Find the email field using xpath without id
email = driver.find_element_by_xpath("//input[@name='email']")
email.send_keys('avinash@qxf2.com')

# Find the phone no field using id
phone = driver.find_element_by_id('phone')
phone.send_keys('9999999999')

# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close() 
        