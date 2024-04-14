from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_icon = (By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/span/span/div/div[1]")

    def is_profile_visible(self):
        return self.driver.find_element(*self.profile_icon).is_displayed()
