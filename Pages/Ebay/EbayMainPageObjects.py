from selenium.webdriver.common.by import By


class EbayMainPageObjects:

    SignInLink = (By.LINK_TEXT, 'Sign in')
    LoggedUserLink = (By.XPATH, '//a[@id="gh-ug"][contains(.,"{0}")]')
