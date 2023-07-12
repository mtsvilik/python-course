from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage


class MyAccountPage(BasePage):
    my_account_name = (By.ID, "nav-link-accountList-nav-line-1")

    def __init__(self, driver):
        super().__init__(driver)

    def get_my_account_name(self):
        return self.get_text(self.my_account_name)
