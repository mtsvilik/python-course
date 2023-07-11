from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_lambdatest_ecommerce():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ecommerce-playground.lambdatest.io/")
    driver.find_element(By.XPATH,
                        "//div[@id='entry_217822']//input[@placeholder='Search For Products']").send_keys("iphone")
    driver.find_element(By.CSS_SELECTOR, "button[class='type-text']").click()
    search_value = driver.find_element(By.XPATH, "//h1[normalize-space()='Search - iphone']").text
    assert "iphone" in search_value
