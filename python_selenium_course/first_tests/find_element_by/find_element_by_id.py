import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

EMAIL = "email"
PASSWORD = "password"


class FindElementById:

    def locate_by_id(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("https://stepik.org/learn?auth=login")
        driver.find_element(By.ID, "id_login_email").send_keys(EMAIL)
        driver.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, "//*[@id='login_form']/button")
        time.sleep(2)
        driver.close()


find_by_id = FindElementById()
find_by_id.locate_by_id()
