from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
url= "http://10.235.11.27/start_b.htm"
driver.get(url)

# Extract the last octet from the URL
ip_part = url.split("//")[-1].split("/")[0]
last_octet = int(ip_part.split('.')[-1])  # Get the last octet as an integer


# Wait for the login page to load and the username field to be visible and clickable
WebDriverWait(driver, 300).until(EC.element_to_be_clickable((By.NAME, "user")))

#finding the user field
user=driver.find_element(By.NAME,"user")
#finding the password field
passwd=driver.find_element(By.NAME,"pw")
#finding the send button
enter=driver.find_element(By.ID,"SendBtn10")

# Sending Key strokes
user.send_keys("admin")
passwd.send_keys("1111")
enter.click()

#Finding IP settings
ip_settings=driver.find_element(By.ID,"navigaText2")

#Defining IPs
data_ip=[10,235,36,last_octet]
data_gw=[10,235,36,1]
data_sm=[255,255,255,224]

ip_settings.click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "ip_network_ip2d")))

#Finding the IP Field to be changed
ip_a=driver.find_element(By.ID,"ip_network_ip2a")
ip_b=driver.find_element(By.ID,"ip_network_ip2b")
ip_c=driver.find_element(By.ID,"ip_network_ip2c")
ip_d=driver.find_element(By.ID,"ip_network_ip2d")

gw_a=driver.find_element(By.ID,"ip_network_gw2a")
gw_b=driver.find_element(By.ID,"ip_network_gw2b")
gw_c=driver.find_element(By.ID,"ip_network_gw2c")
gw_d=driver.find_element(By.ID,"ip_network_gw2d")

sm_a=driver.find_element(By.ID,"ip_network_sm2a")
sm_b=driver.find_element(By.ID,"ip_network_sm2b")
sm_c=driver.find_element(By.ID,"ip_network_sm2c")
sm_d=driver.find_element(By.ID,"ip_network_sm2d")

ips=[ip_a, ip_b, ip_c, ip_d]
for index, ip in enumerate(ips):
    ip.clear()  # Clear existing value
    ip.send_keys(str(data_ip[index]))  # Send corresponding IP from data_ip

gateway=[gw_a, gw_b, gw_c, gw_d]
for index, gw in enumerate(gateway):
    gw.clear()
    gw.send_keys(str(data_gw[index]))

subnet=[sm_a, sm_b, sm_c, sm_d]
for index, sm in enumerate(subnet):
    sm.clear()
    sm.send_keys(str(data_sm[index]))

#network preference button
net_prefer=driver.find_element(By.ID, "ip_network_pref2")
net_prefer.click()


#Defining the 1st interface ids
ip_1a=driver.find_element(By.ID,"ip_network_ip1a")
ip_1b=driver.find_element(By.ID,"ip_network_ip1b")
ip_1c=driver.find_element(By.ID,"ip_network_ip1c")
ip_1d=driver.find_element(By.ID,"ip_network_ip1d")

gw_1a=driver.find_element(By.ID,"ip_network_gw1a")
gw_1b=driver.find_element(By.ID,"ip_network_gw1b")
gw_1c=driver.find_element(By.ID,"ip_network_gw1c")
gw_1d=driver.find_element(By.ID,"ip_network_gw1d")

sm_1a=driver.find_element(By.ID,"ip_network_sm1a")
sm_1b=driver.find_element(By.ID,"ip_network_sm1b")
sm_1c=driver.find_element(By.ID,"ip_network_sm1c")
sm_1d=driver.find_element(By.ID,"ip_network_sm1d")

data_ip_1 = [ip_1a, ip_1b, ip_1c, ip_1d]
gw_ip_1 = [gw_1a, gw_1b, gw_1c, gw_1d]
sm_ip_1 = [sm_1a, sm_1b, sm_1c, sm_1d]

for index, ip in enumerate(data_ip_1):
    ip.clear()  # Clear existing value

for index, ip in enumerate(gw_ip_1):
    ip.clear()  # Clear existing value

for index, ip in enumerate(sm_ip_1):
    ip.clear()


#submitting the changes
submit=driver.find_element(By.ID, "ipinp_send_btn")
submit.click()

#rebooting Pal
reboot_url = "http://10.235.11.27/cgi-bin/xload.cgi?R=0317012"
driver.get(reboot_url)







