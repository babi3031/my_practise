import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    request.cls.driver = driver
    yield
    driver.quit()
