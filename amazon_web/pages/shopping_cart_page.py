from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    cart_is_empty_text = (By.XPATH, "//h2[normalize-space()='Your Amazon Cart is empty']")
    product_title = (By.XPATH, "//span[@class='a-truncate-cut']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_is_empty_text(self):
        return self.get_text(self.cart_is_empty_text)

    def get_product_title(self):
        return self.get_text(self.product_title)
