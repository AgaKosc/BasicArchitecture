import selenium.webdriver as webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class WebdriverFactory:

    @staticmethod
    def getWebdriver(browserName):
        browserName = browserName.lower()
        if browserName == 'firefox':
            binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
            return webdriver.Firefox(firefox_binary=binary)
        elif browserName == 'chrome':
            return webdriver.Chrome()
        elif browserName == 'ie':
            return webdriver.Ie()
        raise Exception("No such '{0}' browser exists".format(browserName))
