from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def get_elements(self, locator):
        elements = WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator))
        return elements

    def set(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_present(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        return bool(element)

    def is_selected(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_located_to_be_selected(locator))
        return bool(element)

    def get_title(self):
        return self.driver.title
