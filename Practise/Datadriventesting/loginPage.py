import utilities
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.implicitly_wait(30)
print("working")
path = ""
driver.close()