from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url= "10.235.11.27"
driver.get("url")
user = driver.find_element(By.NAME, "user")
passwd = driver.find_element(By.NAME, "pass")
enter = driver.find_element(By.NAME, "submit")
user.send_keys("admin")
passwd.send_keys("astro")
enter.submit()
logout = driver.find_element(By.LINK_TEXT, "Logout")

logout.click()
yes_button = driver.find_element(By.NAME, "yes")
yes_button.submit()
time.sleep(10)

#open a new tab
#driver.switch_to.new_window('tab')

# Load a page 
#driver.get('http://stackoverflow.com/')
