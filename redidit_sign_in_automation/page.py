from locators import *

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(*USERNAME).clear()
        self.driver.find_element(*USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*PASSWORD).clear()
        self.driver.find_element(*PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LOGIN).click()
    
    def is_main_page_reached(self):
        return self.driver.find_element(*page_reached).is_displayed()
        