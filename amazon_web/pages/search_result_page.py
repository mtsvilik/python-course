from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage
from amazon_web.pages.product_page import ProductPage


class SearchResultPage(BasePage):
    search_result = (By.CSS_SELECTOR, "[data-image-index='3']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        self.click(self.search_result)
        return ProductPage(self.driver)
