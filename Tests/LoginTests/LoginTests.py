import logging
import random

from Tests.BaseTestCase import BaseTestCase


class LoginTests(BaseTestCase):

    def test_successfulLogin(self):
        logging.info("Test successfulLogin")
        self.page.\
            clickSignInLink().\
            loginWithValidUser(self.envSettings.ebayUser).\
            checkLoggedUser(self.envSettings.ebayUser)

    def test_wrongLogin(self):
        ebayUser = self.envSettings.ebayUser
        ebayUser.login += random.choice('asdf1324')
        messageText = self.page.\
            clickSignInLink().\
            loginWithInvalidUser(ebayUser)
        self.assertEqual("Oops, that's not a match.", messageText)
