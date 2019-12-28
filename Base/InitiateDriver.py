from selenium.webdriver import Chrome
from Library import ConfigReader
def StartBrowser():
    global driver
    path = "C:\\Users\\Kanika Gupta\\Downloads\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get(ConfigReader.read_config("Details", "Application_URL"))
    driver.maximize_window()
    return driver

def CloseBrowser():
    driver.close()