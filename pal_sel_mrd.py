from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url= "http://10.235.11.27/start_b.htm"
driver.get(url)
time.sleep(40)

user=driver.find_element(By.NAME,"user")
passwd=driver.find_element(By.NAME,"pw")
enter=driver.find_element(By.ID,"SendBtn10")



user.send_keys("admin")
passwd.send_keys("1111")
enter.click()
time.sleep(5)
ip_settings=driver.find_element(By.ID,"navigaText2")
data_ip=[10,235,36,27]
data_gw=[10,235,36,1]
data_sm=[255,255,255,224]
ip_settings.click()
time.sleep(5)

ip=driver.find_element(By.ID,"ip_network_ip2d")
gw=driver.find_element(By.ID,"ip_network_gw2d")
#sm=driver.find_element(By.ID,"ip_network_sm2d")

time.sleep(5)

ip.clear()  # Clears any existing value in the IP field
gw.clear()  # Clears any existing value in the GW field
#sm.clear()  # Clears any existing value in the SM field

ip.send_keys(data_ip[3])
gw.send_keys(data_gw[3])
#sm.send_keys(data_sm[3])

time.sleep(60)






'''user = driver.find_element(By.NAME, "user")
passwd = driver.find_element(By.NAME, "pass")
enter = driver.find_element(By.NAME, "submit")
user.send_keys("admin")
passwd.send_keys("astro")
enter.submit()
logout = driver.find_element(By.LINK_TEXT, "Logout")

logout.click()
yes_button = driver.find_element(By.NAME, "yes")
yes_button.submit()
time.sleep(10)'''

#open a new tab
#driver.switch_to.new_window('tab')

# Load a page 
#driver.get('http://stackoverflow.com/')
