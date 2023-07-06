import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByXpath:

    def locate_by_xpath(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://stepik.org/catalog")
        driver.find_element(By.XPATH, "//img[@alt='Facebook']").click()
        time.sleep(2)
        driver.close()


find_by_xpath = FindElementByXpath()
find_by_xpath.locate_by_xpath()
