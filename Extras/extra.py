import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from base.base_page import BasePage


# This page including the extra tests of BuyMe website

class Extra(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def home_screen_assert_error_messages(self):
        # Test the error messages text in email and password fields
        self.click_element(By.CLASS_NAME, 'notSigned')
        self.click_element(By.CSS_SELECTOR, '#ember4955')
        expected_email_text = 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה'
        expected_password_text = 'כל המתנות מחכות לך! אבל קודם צריך מייל וסיסמה'
        email_field = self.click_element(By.ID, 'ember4939')
        password_field = self.click_element(By.ID, 'ember4946')
        assert expected_email_text == email_field.get_attribute()
        assert expected_password_text == password_field.get_attribute()

    def scroll_and_take_screen_shot(self):
        # Scroll to the bottom of the screen, take a screenshot and add it to the report
        element = self.driver.find_element(By.CLASS_NAME, value="newsletter-checkbox ember-view bm-checkbox")
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
