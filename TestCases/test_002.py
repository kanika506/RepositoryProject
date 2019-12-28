from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationData
def test_data():
    driver = InitiateDriver.StartBrowser()

    reg = RegistrationData.RegisterData(driver)
    reg.PasswordName("QWER")
    reg.CpasswordName("QWER")

    # driver = InitiateDriver.CloseBrowser()