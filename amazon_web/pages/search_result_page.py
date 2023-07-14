import random

from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage
from amazon_web.pages.product_page import ProductPage


class SearchResultPage(BasePage):
    result_product_list = (By.XPATH, "//*[contains(@class, 'title-instructions')]")

    def __init__(self, driver):
        super().__init__(driver)

    def click_search_result(self):
        elements = self.get_elements(self.result_product_list)
        result = elements[random.randint(0, len(elements) - 1)]
        result.click()
        return ProductPage(self.driver)
