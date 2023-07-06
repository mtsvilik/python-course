import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class FindElementByCss:

    def locate_by_css(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://stepik.org/catalog")
        driver.find_element(By.CSS_SELECTOR, "img[alt='Twitter']").click()
        time.sleep(4)
        driver.close()


find_by_xpath = FindElementByCss()
find_by_xpath.locate_by_css()
