from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SignupPage(BasePage):

    def enter_email_address(self, email_address):
        self.enter_text((By.XPATH,""),email_address)

    def enter_password(self, password):
        self.enter_text((By.XPATH,""),password)

    def enter_phone_number(self, phone_number):
        self.enter_text((By.XPATH,""),phone_number)

    def enter_full_name(self, full_name):
        self.enter_text((By.XPATH,""),full_name)

    def click_signup(self):
        self.click((By.XPATH,""))

    def signup(self, email, password, full_name, phone_number):
        self.enter_email_address(email)
        self.enter_password(password)
        self.enter_phone_number(phone_number)
        self.enter_full_name(full_name)
        self.click_signup()
