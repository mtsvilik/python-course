from python_pytest_course.lambdatest.pom.pages.base_page import BasePage
from python_pytest_course.lambdatest.pom.pages.my_account_page import MyAccountPage
from python_pytest_course.lambdatest.pom.utilities.locators import ChangePasswordLocatorFields


class ChangePasswordPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locate = ChangePasswordLocatorFields

    def change_password(self, password, confirm_password):
        self.set(self.locate.password_field, password)
        self.set(self.locate.confirm_password_field, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)

    def get_confirmation_error_message(self):
        return self.get_text(self.locate.confirmation_error_message)
