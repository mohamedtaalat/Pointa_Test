from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def enter_email_address(self, email):
        self.enter_text((By.XPATH,""),email)

    def enter_password(self, password):
        self.enter_text((By.XPATH,""),password)

    def click_login(self):
        self.click((By.XPATH,""))

    def login(self, email, password):
        self.enter_email_address(email)
        self.enter_password(password)
        self.click_login()