from selenium.webdriver.common.by import By

from amazon_web.pages.base_page import BasePage


class LanguageCurrencySettingPage(BasePage):
    es_button = (By.XPATH, "//*[@id='icp-language-settings']/div[3]/div/label/span/span/span[1]")
    eur_button = (By.ID, "icp-currency-dropdown_19")
    submit_button = (By.XPATH, "//input[@aria-labelledby='icp-save-button-announce']")
    language_button = (By.XPATH, "//div[normalize-space()='ES']")
    currency_button = (By.XPATH, "//span[contains(text(),'USD')]")
    currency_change_note = (By.ID, "icp-currency-change-note")

    def __init__(self, driver):
        super().__init__(driver)

    def choose_language(self):
        self.click(self.es_button)
        self.click(self.submit_button)

    def get_language_info(self):
        return self.get_text(self.language_button)

    def choose_currency(self):
        self.click(self.currency_button)
        self.click(self.eur_button)
        self.click(self.submit_button)

    def get_currency_info(self):
        return self.get_text(self.currency_change_note)
