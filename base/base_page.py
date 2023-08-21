class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, locator_type, locator_value):
        self.driver.find_element(locator_type, locator_value).click()

    def click_elements(self, locator_type, locator_value, index):
        self.driver.find_elements(locator_type, locator_value)[index].click()

    def enter_text(self, locator_type, locator_value, text):
        self.driver.find_element(locator_type, locator_value).send_keys(text)

    def enter_texts(self, locator_type, locator_value, index, text):
        self.driver.find_elements(locator_type, locator_value)[index].send_keys(text)
