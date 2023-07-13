from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage


class ShoppingCartPage(BasePage):
    cart_is_empty_text = (By.XPATH, "//h2[normalize-space()='Your Amazon Cart is empty']")
    product_title = (By.XPATH, "//span[@class='a-truncate-cut']")
    value = (By.CSS_SELECTOR, ".a-dropdown-prompt")
    choose_quantity_button = (By.ID, "a-autoid-0-announce")
    quantity_button = (By.ID, "quantity_2")

    def __init__(self, driver):
        super().__init__(driver)

    def get_cart_is_empty_text(self):
        return self.get_text(self.cart_is_empty_text)

    def get_product_title(self):
        return self.get_text(self.product_title)

    def choose_quantity(self):
        self.click(self.choose_quantity_button)
        self.click(self.quantity_button)

    def get_value(self):
        return self.get_text(self.value)
