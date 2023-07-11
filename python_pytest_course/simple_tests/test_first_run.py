import pytest
from selenium import webdriver


@pytest.mark.sanity
def test_google_run():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
