from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(3)
cred=driver.find_element(By.ID,"email")
psw=driver.find_element(By.ID,"pass")
# Entering ID & Password
cred.clear()
cred.send_keys("9430206561")
psw.clear()
psw.send_keys("Vishal3637")
psw.send_keys(Keys.ENTER)
time.sleep(2)
driver.save_screenshot("Error1.png")
time.sleep(10)
