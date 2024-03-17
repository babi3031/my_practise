from selenium.webdriver.common.by import By
from Practise.POMprojectDemo.Locators.locators import Locators
class Homepage():

    def __init__(self,driver):
        self.driver = driver
        self.header = Locators.header_xpath
        self.logout = Locators.logout_link_text

    def click_header(self):
        self.driver.find_element(By.XPATH, self.header).click()

    def click_logout(self):
        self.driver.find_element(By.LINK_TEXT, self.logout).click()