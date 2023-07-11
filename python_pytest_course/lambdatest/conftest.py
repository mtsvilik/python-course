import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox", "safari"])
def initialize_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "safari":
        driver = webdriver.Safari()
    else:
        print("Provide valid browser")

    request.cls.driver = driver
    print("Browser: ", request.param)
    yield
    print("Close driver")
    driver.close()
