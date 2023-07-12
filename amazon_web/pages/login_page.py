from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage
from amazon_web.pages.my_account_page import MyAccountPage


class LoginPage(BasePage):
    email_address_field = (By.ID, "ap_email")
    continue_button = (By.ID, "continue")
    password_field = (By.ID, "ap_password")
    sign_in_button = (By.ID, "signInSubmit")
    warning_message = (By.XPATH, "//h4[normalize-space()='There was a problem']")

    def __init__(self, driver):
        super().__init__(driver)

    def set_email(self, email):
        self.set(self.email_address_field, email)
        self.click(self.continue_button)

    def set_password(self, password):
        self.set(self.password_field, password)

    def click_sign_in_button(self):
        self.click(self.sign_in_button)
        return MyAccountPage(self.driver)

    def get_warning_message(self):
        return self.get_text(self.warning_message)
