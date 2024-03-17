from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from Practise.POMprojectDemo.Pages.loginPage import LoginPage
from Practise.POMprojectDemo.Pages.homePage import Homepage
import HtmlTestRunner

class Logintest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_01_testLoginValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        home = Homepage(self.driver)
        home.click_header()
        home.click_logout()
        # self.driver.find_element(By.NAME,"username").send_keys("Admin")
        # self.driver.find_element(By.NAME,"password").send_keys("admin123")
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img').click()
        # self.driver.find_element(By.LINK_TEXT,'Logout').click()
        driver.implicitly_wait(30)
        time.sleep(5)

    def test_02_testLoginInValid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin1234")
        login.click_login()
        message = login.invalid_credentails()
        self.assertEqual(message,"Invalid credentialss")
        # self.driver.find_element(By.NAME,"username").send_keys("Admin")
        # self.driver.find_element(By.NAME,"password").send_keys("admin123")
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        # self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img').click()
        # self.driver.find_element(By.LINK_TEXT,'Logout').click()
        driver.implicitly_wait(30)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Babi/Reports'))

