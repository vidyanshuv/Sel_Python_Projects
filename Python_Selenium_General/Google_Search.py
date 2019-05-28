from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get("https://www.google.com")
driver.maximize_window()
driver.implicitly_wait(3)
sb=driver.find_element_by_name("q")
sb.send_keys("Selenium + Python")
sb.send_keys(Keys.ENTER)
time.sleep(2)
driver.quit()
