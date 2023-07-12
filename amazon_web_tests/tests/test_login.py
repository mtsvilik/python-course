from python_pytest_course.lambdatest.pom.pages.login_page import LoginPage
from python_pytest_course.lambdatest.pom.tests.base_test import BaseTest
from python_pytest_course.lambdatest.pom.utilities.data import TestData


class TestLogin(BaseTest):
    def test_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.set_email(TestData.email)
        login_page.set_password(TestData.password)
        login_page.click_login_button()
        actual_title = login_page.get_title()
        assert actual_title == "My Account"

    def test_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.log_into_account("Invalid Email", "Invalid Password")
        actual_message = login_page.get_warning_message()
        assert actual_message.__contains__("Warning")

