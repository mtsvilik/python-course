import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("value1, value2, expected_result",
                         [
                             ("25", "25", "50"),
                             ("10", "10", "20"),
                             ("11", "1", "13")
                         ])
def test_two_input_fields(value1, value2, expected_result):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/simple-form-demo")

    driver.find_element(By.ID, "sum1").send_keys(value1)
    driver.find_element(By.ID, "sum2").send_keys(value2)
    driver.find_element(By.XPATH, "//button[normalize-space()='Get Sum']").click()
    result = driver.find_element(By.ID, "addmessage").text
    assert expected_result == result, "Actual and Expected Do not Match"


@pytest.mark.parametrize("base", [1, 2, 3])
@pytest.mark.parametrize("exponent", [4, 5, 6])
def test_raising_base_to_power(base, exponent):
    result = base ** exponent
    assert result == math.pow(base, exponent)
