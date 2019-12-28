from Library import ConfigReader

class RegisterData():

    def __init__(self,obj):
        global driver
        driver = obj
    def UsernameName(self,username):
        driver.find_element_by_name(ConfigReader.FetchElementLocator("ElementLocate", "username_name")).send_keys(
            username)

    def EmailName(self,emailname):
        driver.find_element_by_name(ConfigReader.FetchElementLocator("ElementLocate", "email_name")).send_keys(
            emailname)

    def PasswordName(self,passwordname):
        driver.find_element_by_name(ConfigReader.FetchElementLocator("ElementLocate", "password_name")).send_keys(
            passwordname)

    def CpasswordName(self,cpasswordname):
        driver.find_element_by_name(ConfigReader.FetchElementLocator("ElementLocate", "cpassword_name")).send_keys(
            cpasswordname)