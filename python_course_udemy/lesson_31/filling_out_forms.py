from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Maryia")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Tsvilik")

email = driver.find_element(By.NAME, "email")
email.send_keys("maryia@gmail.com")

sign_up = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up.click()


driver.quit()
