from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# driver = webdriver.Firefox()

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://www.amazon.com/")
driver.maximize_window()
print(driver.title)

driver.close()
