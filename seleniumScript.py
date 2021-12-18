from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time  
from selenium.webdriver.common.keys import Keys  
print("test case started")  
#open Google Chrome browser  
driver = webdriver.Chrome(ChromeDriverManager().install()) 
driver.maximize_window()  

driver.get("http://104.200.30.6/")  
time.sleep(3) 

driver.get("http://104.200.30.6/about/")  
time.sleep(3) 

driver.get("http://104.200.30.6/listings/")  
time.sleep(3) 

driver.get("http://104.200.30.6/")  
time.sleep(3) 

driver.find_element_by_name("keywords").send_keys('pool')  
time.sleep(3)  

driver.find_element_by_xpath("/html/body/section[2]/div/div/div/div/form/button").send_keys(Keys.ENTER)  
time.sleep(3)

driver.get("http://104.200.30.6/")  
time.sleep(3) 

driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[1]/a").send_keys(Keys.ENTER)  
time.sleep(3)

driver.find_element_by_name("first_name").send_keys('piyush')  
time.sleep(1) 

driver.find_element_by_name("last_name").send_keys('pawar')  
time.sleep(1)

driver.find_element_by_name("username").send_keys('piyush')  
time.sleep(1)

driver.find_element_by_name("email").send_keys('piyushpawar199954@gmail.com')  
time.sleep(1)

driver.find_element_by_name("password").send_keys('1234')  
time.sleep(1)

driver.find_element_by_name("password2").send_keys('1234')  
time.sleep(3)

driver.find_element_by_xpath("/html/body/section[2]/div/div/div/div/div[2]/form/input[2]").send_keys(Keys.ENTER)  
time.sleep(3)

driver.close() 