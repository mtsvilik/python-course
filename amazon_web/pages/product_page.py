from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage
from amazon_web.pages.shopping_cart_page import ShoppingCartPage


class ProductPage(BasePage):
    add_to_cart_button = (By.XPATH, "//div[@id='renewedTier2AccordionRow']//input[@id='add-to-cart-button']")
    go_to_cart_button = (By.XPATH, "//a[@href='/cart?ref_=ewc_gtc']")
    cart_button = (By.CSS_SELECTOR, "input[aria-labelledby='attach-sidesheet-view-cart-button-announce']")
    product_cart_element = (By.ID, "attach-desktop-sideSheet")

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self):
        self.click(self.add_to_cart_button)
        if self.is_present(self.product_cart_element):
            self.click(self.cart_button)
        else:
            self.click(self.go_to_cart_button)
        return ShoppingCartPage(self.driver)
