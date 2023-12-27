import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


# This page including the functions of pick_business_page in BuyMe website

class BusinessPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def url_assertion(self):
        expected_url = 'https://buyme.co.il/search?budget=1&category=438&region=11'
        assert expected_url == self.driver.current_url

    def pick_business(self):
        self.click_elements(By.CLASS_NAME, 'bottom', 4)

    def enter_price(self, price):
        self.enter_text(By.CSS_SELECTOR, 'input[type=tel]', price)

    def click_choice_button(self):
        self.click_element(By.CSS_SELECTOR, 'button[type=submit]')
