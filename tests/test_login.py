import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
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

    def test_title(self):
        print(self.driver)
        actual_title = self.driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_placeholder(self):
        actual_username_placeholder= self.driver.find_element(By.ID,"authUser").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute("placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)

