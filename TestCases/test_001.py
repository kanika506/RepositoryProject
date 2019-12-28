from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationData
from DataGenerator import DataGen
import pytest
# def test_data():
#     driver = InitiateDriver.StartBrowser()
#
#     reg = RegistrationData.RegisterData(driver)
#     reg.UsernameName("Kanika Gupta")
#     reg.EmailName("a@gmail.com")
#
#     driver = InitiateDriver.CloseBrowser()

# Data Driven Testing with static data
#
# def Static_data():
#      l = [['user1','pass1'],['user2','pass2'],['user3','pass3']]
#      return l

@pytest.mark.parametrize('data',DataGen.Data_generator())
def test_data(data):
    driver = InitiateDriver.StartBrowser()
    reg = RegistrationData.RegisterData(driver)
    reg.UsernameName(data[0])
    reg.EmailName(data[1])
    # driver = InitiateDriver.CloseBrowser()

