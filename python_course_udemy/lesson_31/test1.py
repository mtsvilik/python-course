from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".medium-widget time")
for time in event_times:
    print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, ".medium-widget li a")
for name in event_names:
    print(name.text)

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.close()
