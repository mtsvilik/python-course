from amazon_web.pages.home_page import HomePage
from amazon_web.tests.base_test import BaseTest
from amazon_web.utils.test_data import TestData


class TestAmazonWeb(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_sign_in_button()
        login_page.set_email(TestData.email)
        login_page.set_password(TestData.password)
        my_account_page = login_page.click_sign_in_button()
        actual_name = my_account_page.get_my_account_name()
        assert actual_name.__contains__(TestData.name)

    def test_login_with_invalid_credentials(self):
        home_page = HomePage(self.driver)
        login_page = home_page.click_sign_in_button()
        login_page.set_email(TestData.invalid_email)
        actual_message = login_page.get_warning_message()
        assert actual_message == TestData.warning_message

    def test_cart_button_is_clickable(self):
        home_page = HomePage(self.driver)
        shopping_cart_page = home_page.click_shopping_cart_button()
        actual_text = shopping_cart_page.get_cart_is_empty_text()
        assert actual_text == TestData.text

    def test_product_is_added_to_cart(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.open_result_page(TestData.search_text)
        product_page = search_result_page.click_search_result()
        shopping_cart_page = product_page.add_product_to_cart()
        actual_title = shopping_cart_page.get_product_title()
        assert actual_title.__contains__(TestData.product_title)

    def test_increase_product_in_cart(self):
        home_page = HomePage(self.driver)
        search_result_page = home_page.open_result_page(TestData.search_text)
        product_page = search_result_page.click_search_result()
        shopping_cart_page = product_page.add_product_to_cart()
        shopping_cart_page.choose_quantity()
        actual_quantity = shopping_cart_page.get_value()
        assert actual_quantity == TestData.quantity

    def test_change_language(self):
        home_page = HomePage(self.driver)
        language_currency_setting_page = home_page.click_change_language_button()
        language_currency_setting_page.choose_language()
        actual_language = language_currency_setting_page.get_language_info()
        assert actual_language == TestData.language

    def test_change_currency(self):
        home_page = HomePage(self.driver)
        language_currency_setting_page = home_page.click_change_currency_button()
        language_currency_setting_page.choose_currency()
        actual_currency = language_currency_setting_page.get_currency_info()
        assert actual_currency.__contains__(TestData.currency)
