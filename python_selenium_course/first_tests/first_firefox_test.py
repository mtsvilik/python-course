from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.amazon.com/")
driver.maximize_window()
print(driver.title)

driver.close()
