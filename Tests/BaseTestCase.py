import unittest
import logging
from datetime import datetime
import sys

from selenium.webdriver.support.ui import WebDriverWait


class BaseTestCase(unittest.TestCase):

    waitTime = 30

    def setUp(self, browser='chrome', env='prod'):
        from Pages.Ebay.EbayMainPage import EbayMainPage
        from Helpers.Factories.SettingsFactory import SettingsFactory
        from Helpers.Factories.WebdriverFactory import WebdriverFactory
        logging.basicConfig(level=logging.INFO)
        self.envSettings = SettingsFactory.getSettings(env)
        self.ebayDriver = WebdriverFactory.getWebdriver(browser)
        self.ebayDriver.maximize_window()
        self.ebayDriver.get(self.envSettings.ebayUrl)
        self.wait = WebDriverWait(self.ebayDriver, self.waitTime)
        self.page = EbayMainPage(self.ebayDriver)

    def tearDown(self):
        if sys.exc_info()[0]:
            tcName = self._testMethodName
            creationTime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            self.ebayDriver.get_screenshot_as_file("E:/Reports/{0}_{1}.jpg".format(tcName, creationTime))
        self.ebayDriver.quit()
