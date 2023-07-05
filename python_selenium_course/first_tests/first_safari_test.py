from selenium import webdriver

driver = webdriver.Safari()

driver.get("https://www.amazon.com/")
driver.maximize_window()
print(driver.title)

driver.close()
