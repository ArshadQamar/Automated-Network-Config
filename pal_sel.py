from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


urls=["http://10.235.11.9",
    "http://10.235.11.10",
    "http://10.235.11.11",]
driver = webdriver.Chrome()
print(f"navigatin to {urls[0]}")
driver.get(urls[0]) #opening 1st url


for url in urls[1:]: #iterating from 2nd url
    driver.switch_to.new_window('window')
    print(f"navigatin to {url}")
    driver.get(url)
    
time.sleep(180)