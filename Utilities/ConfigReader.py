from configparser import ConfigParser
import os


def readConfig(section, key):
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'Configuration/config.ini'))
    return config.get(section, key)

# print(readConfig("paths", "login.url"))
