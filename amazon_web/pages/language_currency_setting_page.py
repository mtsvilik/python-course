import random

from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage


class LanguageCurrencySettingPage(BasePage):
    result_language_list = (By.XPATH, "//*[@class='a-label a-radio-label']")
    result_currency_list = (By.XPATH, "//*[@class='a-dropdown-link']")
    submit_button = (By.XPATH, "//input[@aria-labelledby='icp-save-button-announce']")
    language_button = (By.XPATH, "//div[normalize-space()='ES']")
    currency_button = (By.XPATH, "//span[contains(text(),'USD')]")
    currency_change_note = (By.ID, "icp-currency-change-note")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_language(self):
        elements = self.get_elements(self.result_language_list)
        result = elements[random.randint(0, len(elements) - 1)]
        result.click()
        self.click(self.submit_button)

    def get_language_info(self):
        return self.get_text(self.language_button)

    def choose_currency(self):
        self.click(self.currency_button)
        elements = self.get_elements(self.result_currency_list)
        print(elements)
        result = elements[random.randint(0, len(elements) - 1)]
        result.click()
        self.click(self.submit_button)

    def get_currency_info(self):
        return self.get_text(self.currency_change_note)
