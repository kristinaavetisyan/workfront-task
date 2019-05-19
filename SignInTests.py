import unittest
from selenium import webdriver

class SignIn(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\Kristina\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.browser.get("https://ancient-taiga-22967.herokuapp.com/")

    def test_signing_in_valid_credentials(self):
        self.search_element = self.browser.find_element_by_link_text("Sign in")
        self.search_element.click()

        self.username = self.browser.find_element_by_id("email")
        self.username.send_keys("mail@email.com")
        self.password = self.browser.find_element_by_id("password")
        self.password.send_keys("test123")

        self.submit = self.browser.find_element_by_class_name("form-actions")
        self.submit.click()

        assert self.browser.current_url == "https://ancient-taiga-22967.herokuapp.com/user/todos"

    def test_signing_in_invalid_credentials(self):
        self.search_element = self.browser.find_element_by_link_text("Sign in")
        self.search_element.click()

        self.username = self.browser.find_element_by_id("email")
        self.username.send_keys("wrong@email.com")
        self.password = self.browser.find_element_by_id("password")
        self.password.send_keys("invalidpassword")

        self.submit = self.browser.find_element_by_class_name("form-actions")
        self.submit.click()

        assert self.browser.current_url == "https://ancient-taiga-22967.herokuapp.com/login.do"

    def tearDown(self):
         self.browser.quit()



if __name__ == '__main__':
    unittest.main()
