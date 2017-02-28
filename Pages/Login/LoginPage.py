import logging
from Pages.BasePage import BasePage
from Pages.Login.LoginPageObjects import LoginPageObjects


class LoginPage(BasePage):

    def __login(self, user):
        logging.debug('logging into ebay with credentials: {0} // {1}'.format(user.login, user.password))
        self.driver.find_element(*LoginPageObjects.LoginInput).clear()
        self.driver.find_element(*LoginPageObjects.LoginInput).send_keys(user.login)
        self.driver.find_element(*LoginPageObjects.PasswordInput).clear()
        self.driver.find_element(*LoginPageObjects.PasswordInput).send_keys(user.password)
        self.driver.find_element(*LoginPageObjects.SignInButton).click()

    def loginWithValidUser(self, user):
        from Pages.Ebay.EbayMainPage import EbayMainPage
        self.__login(user)
        return EbayMainPage(self.driver)

    def loginWithInvalidUser(self, user):
        self.__login(user)
        messageText = self.driver.find_element(*LoginPageObjects.LoginErrorMessage).text
        return messageText
