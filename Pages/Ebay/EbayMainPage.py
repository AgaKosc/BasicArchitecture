import logging
from Pages.BasePage import BasePage
from Pages.Ebay.EbayMainPageObjects import EbayMainPageObjects


class EbayMainPage(BasePage):

    def clickSignInLink(self):
        from Pages.Login.LoginPage import LoginPage
        logging.info("Clicking in sign in link")
        self.driver.find_element(*EbayMainPageObjects.SignInLink).click()
        return LoginPage(self.driver)

    def checkLoggedUser(self, user):
        logging.info("Checking logged user")
        self.driver.find_element(EbayMainPageObjects.LoggedUserLink[0],
                                 EbayMainPageObjects.LoggedUserLink[1].format(user.name))
        return self
