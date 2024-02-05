import pytest
from selenium import webdriver

"""Code helps to configure browser for all test methods"""


class WebDriverWrapper:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # runs before each test_method
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get("https://demo.openemr.io/b/openemr")
        yield
        # runs after each testt_method
        self.driver.quit()
