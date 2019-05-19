import unittest
from selenium import webdriver

class CreateTodo(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\Users\\Kristina\\Downloads\\chromedriver_win32\\chromedriver.exe")
        self.browser.get("https://ancient-taiga-22967.herokuapp.com/user/todos")

    def user_signin(self):
        self.browser.get("https://ancient-taiga-22967.herokuapp.com")
        self.browser.implicitly_wait(10)
        self.search_element = self.browser.find_element_by_link_text("Sign in")
        self.search_element.click()

        self.username = self.browser.find_element_by_id("email")
        self.username.send_keys("mail@email.com")
        self.password = self.browser.find_element_by_id("password")
        self.password.send_keys("test123")

        self.submit = self.browser.find_element_by_class_name("form-actions")
        self.submit.click()


    def test_creating_todo(self):
        self.user_signin()
        assert self.browser.current_url == "https://ancient-taiga-22967.herokuapp.com/user/todos"

        self.search_element = self.browser.find_element_by_xpath('//div[2]/div/div[1]/div/ul/li[4]/a/i')
        self.search_element.click()

        assert self.browser.current_url == "https://ancient-taiga-22967.herokuapp.com/user/todos/new"

        self.title = self.browser.find_element_by_xpath('//*[@id="title"]')
        self.title.send_keys("task1")

        self.date = self.browser.find_element_by_xpath('//*[@id="dueDate"]')
        self.date.send_keys("07/05/2014")

        self.priority = self.browser.find_element_by_xpath('//*[@id="priority"]')
        self.priority.send_keys("MEDIUM")

        self.create = self.browser.find_element_by_xpath('//*[@id="createTodoForm"]/fieldset/div[4]/button[1]')
        self.create.click()

        assert self.browser.current_url == "https://ancient-taiga-22967.herokuapp.com/user/todos"

    def tearDown(self):
         self.browser.quit()

if __name__ == '__main__':
    unittest.main()