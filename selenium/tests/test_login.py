import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_login(self):
        self.driver.implicitly_wait(25)  # Again, explicit waits are a better approach
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        # You should use environment variables or secure ways to handle credentials
        login_page.enter_username("7659863220")
        login_page.enter_password("***********")
        login_page.click_login()

        assert home_page.is_profile_visible()
