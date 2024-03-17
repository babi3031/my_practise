from selenium.webdriver.common.by import By
from Practise.POMprojectDemo.Locators.locators import Locators
class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.username = Locators.username_name
        self.password = Locators.password_name
        self.login = Locators.login_xpath
        self.invalid_credentail =  Locators.invalid_xpath

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username).clear()
        self.driver.find_element(By.NAME, self.username).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.password).clear()
        self.driver.find_element(By.NAME, self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.login).click()

    def invalid_credentails(self):
        msg = self.driver.find_element(By.XPATH,self.invalid_credentail).text
        print(msg)
        return msg