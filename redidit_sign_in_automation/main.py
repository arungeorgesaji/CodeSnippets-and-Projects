import unittest
from selenium import webdriver
from page import LoginPage
from selenium.webdriver.chrome.service import Service

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        service = Service("C:\\Users\\DELL\\Downloads\\chromedriver\\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.get("https://www.reddit.com/login/")
        
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username("")
        login_page.enter_password("")
        login_page.click_login_button()
        self.driver.implicitly_wait(6)
        
        self.assertTrue(login_page.is_main_page_reached(), "wrong credentials")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()