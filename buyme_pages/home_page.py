import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage


# This page including the functions of home_page in BuyMe website

class HomePage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def click_price_dropdown(self):
        self.click_elements(By.CLASS_NAME, 'selected-name', 0)

    def choose_price(self):
        self.click_element(By.ID, 'ember1075')

    def click_region_dropdown(self):
        self.click_elements(By.CLASS_NAME, 'selected-name', 1)

    def choose_region(self):
        self.click_element(By.ID, 'ember1111')

    def click_category_dropdown(self):
        self.click_elements(By.CLASS_NAME, 'selected-name', 2)

    def choose_category(self):
        self.click_element(By.ID, 'ember1180')

    def click_find_me_gift_button(self):
        self.click_element(By.CSS_SELECTOR, 'a[rel=nofollow]')
