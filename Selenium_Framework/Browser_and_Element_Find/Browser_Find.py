from selenium import webdriver
class Browser():
    def ChooseBrowser(arg):
        arg=arg.lower()
        import os
        if arg=="chrome":
            return webdriver.Chrome()
        elif arg=="firefox":
            return webdriver.Firefox()
        elif arg=="ie":
            driverLocation = "C:\\Users\\anshu\\Documents\\Python_Projects\\Drivers\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = driverLocation
            driver = "webdriver.Ie(driverLocation)"
            return webdriver.Ie(driverLocation)

