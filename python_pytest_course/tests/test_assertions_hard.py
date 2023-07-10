from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionsTest:
    pass


def test_radio_button_value():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")

    driver.find_element(By.CSS_SELECTOR, "input[value='Female'][name='gender']").click()
    driver.find_element(By.CSS_SELECTOR, "input[value='15 - 50']").click()
    driver.find_element(By.XPATH, "//button[normalize-space()='Get values']").click()

    gender = driver.find_element(By.CSS_SELECTOR, ".genderbutton").text
    age_group = driver.find_element(By.CSS_SELECTOR, ".groupradiobutton").text

    print("Gender Object: \t", id(gender))
    print("Male Object: \t", id("Female"))
    assert gender is "Female", "Gender is not correct"

    assert driver.title.__contains__("Selenium Grid Online")
    assert "51" in age_group, "Age group is not correct"
