import softest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AssertionsTest(softest.TestCase):
    pass

    def test_radio_button(self):
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

        self.soft_assert(self.assertEquals,
                         "Female", gender, "Gender Is Not Correct")
        self.soft_assert(self.assertTrue,
                         driver.title.__contains__("Selenium Grid Online"))
        # self.soft_assert(self.assertEquals,
        #                  "51", age_group, "Age Group Is Not Correct")
        self.assert_all("Verify Gender, Title, & Age Group")
