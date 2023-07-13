import pytest
from selenium import webdriver
from amazon_web.utils.test_data import TestData


@pytest.fixture(params=["chrome", "firefox"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Provide valid browser")

    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.get(TestData.url)
    driver.maximize_window()
    yield
    print("Close driver")
    driver.close()
