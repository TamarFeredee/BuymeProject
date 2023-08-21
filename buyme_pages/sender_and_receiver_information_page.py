import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


# This page including the functions of sender_and_receiver_information_page in BuyMe website
class SenderAndReceiverPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_for_someone_else_button(self):
        time.sleep(3)
        self.click_element(By.ID, 'ember1370')

    def enter_receiver_name(self, receiver_name):
        time.sleep(3)
        expected_receiver_name = receiver_name
        element = self.enter_text(By.ID, 'friendName', receiver_name)
        time.sleep(3)
        assert expected_receiver_name == element.get_attribute()

    def click_dropdown_events(self):
        time.sleep(5)
        self.click_element(By.CLASS_NAME, 'selected-name')

    def choose_event(self):
        time.sleep(5)
        self.click_element(By.ID, 'ember1802')

    def enter_blessing(self, words):
        time.sleep(3)
        self.enter_text(By.ID, 'ember1385', words)

    def click_upload_picture_button(self, screenshot_path):
        time.sleep(5)
        self.enter_text(By.XPATH, '//*[@id="ember2475"]', screenshot_path)
        time.sleep(5)

    def click_continue_button(self):
        time.sleep(3)
        self.click_element(By.ID, 'ember1395')

    def click_on_now_checkbox(self):
        time.sleep(3)
        self.click_element(By.CLASS_NAME, 'check')

    def click_on_email_button(self):
        time.sleep(3)
        self.click_element(By.CSS_SELECTOR, 'svg[gtm=method-email]')

    def enter_receiver_email(self, receiver_email):
        time.sleep(3)
        self.enter_text(By.ID, 'email', receiver_email)

    def enter_sender_name(self, sender_name):
        time.sleep(3)
        self.enter_text(By.CSS_SELECTOR, 'input[type=text', sender_name)
        time.sleep(3)
