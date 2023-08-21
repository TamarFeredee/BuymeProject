import json
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from Extras.extra import Extra
from buyme_pages.home_page import HomePage
from buyme_pages.intro_and_registration_page import IntroPage
from buyme_pages.pick_business_page import BusinessPage
from buyme_pages.sender_and_receiver_information_page import SenderAndReceiverPage


# This page including the tests of BuyMe website
class BuyMeTests(unittest.TestCase):
    # setUp - all the preconditions before running the tests and relevant for each test
    def setUp(self):
        # read browserType&URL from config.json file + define the test to run in incognito&start-maximized mode
        json_file = open('config.json', 'r')
        data = json.load(json_file)
        browser = data['browserType']
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--start-maximized")
        if browser == 'chrome':
            self.driver = webdriver.Chrome(
                service=Service("/Users/tamarferede/Downloads/chromedriver_mac_arm64/chromedriver"),
                options=chrome_options)
        url = data['URL']
        self.driver.get(url)

        # implicit wait
        self.driver.implicitly_wait(10)
        # page load timeout
        self.driver.set_page_load_timeout(10)

        self.home_page = HomePage(self.driver)
        self.intro_page = IntroPage(self.driver)
        self.business_page = BusinessPage(self.driver)
        self.sender_and_receiver_page = SenderAndReceiverPage(self.driver)
        self.extra = Extra(self.driver)

    # Testing the functionality of the intro_and_registration_page
    def test_01_intro_page(self):
        self.intro_page.click_signin_area()
        self.intro_page.click_signin_button()
        self.intro_page.fill_registration_details('tamar', 'tamar@test.com', '123456', '123456')
        self.intro_page.click_on_terms_and_conditions_checkbox_button()
        self.intro_page.click_registration_button()

    # Testing the functionality of the home_page
    def test_02_home_page(self):
        self.home_page.click_price_dropdown()
        self.home_page.choose_price()
        self.home_page.click_region_dropdown()
        self.home_page.choose_region()
        self.home_page.click_category_dropdown()
        self.home_page.choose_category()
        self.home_page.click_find_me_gift_button()

    # Testing the functionality of the pick_business_page
    def test_03_business_page(self):
        time.sleep(3)
        self.driver.get('https://buyme.co.il/search?budget=1&category=438&region=11')
        self.business_page.url_assertion()
        self.business_page.pick_business()
        self.business_page.enter_price(500)
        self.business_page.click_choice_button()

    # Testing the functionality of the sender_and_receiver_information_page
    def test_04_sender_and_receiver_page(self):
        time.sleep(3)
        self.driver.get('https://buyme.co.il/money/1229712?price=500')
        self.sender_and_receiver_page.click_for_someone_else_button()
        self.sender_and_receiver_page.enter_receiver_name('tamar')
        self.sender_and_receiver_page.click_dropdown_events()
        self.sender_and_receiver_page.choose_event()
        self.sender_and_receiver_page.enter_blessing('מזל טוב')
        self.sender_and_receiver_page.click_upload_picture_button(
            '/Users/tamarferede/Desktop/Screen Shot 2023-08-17 at 9.27.05.png')
        self.sender_and_receiver_page.click_continue_button()
        self.sender_and_receiver_page.click_on_now_checkbox()
        self.sender_and_receiver_page.click_on_email_button()
        self.sender_and_receiver_page.enter_receiver_email('tamar@test.com')
        self.sender_and_receiver_page.enter_sender_name('tami')

    # Testing the error messages text in email and password fields
    def test_05_error_messages_text(self):
        self.extra.home_screen_assert_error_messages()

    # Scroll to the bottom of the screen, take a screenshot and add it to the report
    def test_06_scroll_and_take_screen_shot(self):
        self.extra.scroll_and_take_screen_shot()

    # finishing all the test by quiting the browser
    def tearDown(self):
        self.driver.quit()
