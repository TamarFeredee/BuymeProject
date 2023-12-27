import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


# This page including the functions of intro_and_registration_page in BuyMe website

class IntroPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_signin_area(self):
        self.click_element(By.CLASS_NAME, 'notSigned')

    def click_signin_button(self):
        self.click_element(By.CSS_SELECTOR, 'span[aria-label=להרשמה]')

    def fill_registration_details(self, first_name, email, password, password_confirmation):
        expected_name = first_name
        element = self.enter_text(By.ID, 'ember1917', first_name)
        assert expected_name == element.get_attribute()
        self.enter_text(By.ID, 'ember1924', email)
        self.enter_text(By.ID, 'valPass', password)
        self.enter_text(By.ID, 'ember1938', password_confirmation)

    def click_on_terms_and_conditions_checkbox_button(self):
        self.click_element(By.ID, 'ember1944')

    def click_registration_button(self):
        self.click_element(By.ID, 'ember1948')
