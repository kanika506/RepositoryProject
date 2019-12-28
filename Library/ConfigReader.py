from configparser import ConfigParser

def read_config(section,key):
    config = ConfigParser()
    config.read("../ConfigurationFiles/Config.cfg")
    return config.get(section,key)

def FetchElementLocator(section,key):
    config = ConfigParser()
    config.read("../ConfigurationFiles/Element.cfg")
    return config.get(section, key)
