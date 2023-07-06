from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=lp_16225009011_1_3?sbo=RZvfv%2F%2FHxDF%2BO5021pAnSA%3D%3D")
price = driver.find_element(By.XPATH, "//*[@id='corePrice_desktop']/div/table/tbody/tr/td[2]/span[1]/span[2]")
print(price.text)

# driver.close()
driver.quit()