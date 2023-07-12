from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage
from amazon_web.pages.login_page import LoginPage
from amazon_web.pages.search_result_page import SearchResultPage
from amazon_web.pages.shopping_cart_page import ShoppingCartPage


class HomePage(BasePage):
    sign_in_button = (By.ID, "nav-link-accountList-nav-line-1")
    shopping_cart_button = (By.ID, "nav-cart-count")
    search_field = (By.ID, "twotabsearchtextbox")
    search_button = (By.ID, "nav-search-submit-button")

    def __init__(self, driver):
        super().__init__(driver)

    def click_sign_in_button(self):
        self.click(self.sign_in_button)
        return LoginPage(self.driver)

    def click_shopping_cart_button(self):
        self.click(self.shopping_cart_button)
        return ShoppingCartPage(self.driver)

    def open_result_page(self, search_text):
        self.set(self.search_field, search_text)
        self.click(self.search_button)
        return SearchResultPage(self.driver)
