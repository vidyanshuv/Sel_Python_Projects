from selenium import webdriver
from selenium.webdriver.common.by import By

class Find_Element():
    def __init__(self, driver):
        self.driver = driver

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            if locatorType == "id":
                element = self.driver.find_element(By.ID, locator)
                return element
            elif locatorType == "name":
                element = self.driver.find_element(By.NAME, locator)
                return element
            elif locatorType == "xpath":
                element = self.driver.find_element(By.XPATH, locator)
                return element
            elif locatorType == "css":
                element =self.driver.find_element(By.CSS_SELECTOR, locator)
                return element
            elif locatorType == "classname":
                element =self.driver.find_element(By.CLASS_NAME, locator)
                return element
            elif locatorType == "linktext":
                element =self.driver.find_element(By.LINK_TEXT, locator)
                return element
            else:
                print("Locator type " + locatorType + " not correct/supported")
        except:
            print("Element not found")
