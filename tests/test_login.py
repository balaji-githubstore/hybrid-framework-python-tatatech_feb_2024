import pytest
from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.automation_wrapper import WebDriverWrapper
from pages.login_page import LoginPage
from utils.data_utils import DataSource


class TestLogin(WebDriverWrapper):

    @pytest.mark.parametrize("username,password,expected_title", DataSource.data_valid_login)
    def test_valid_login(self, username, password, expected_title):

        login=LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)
        self.driver.find_element(By.ID, "login-button").click()
        assert_that(expected_title).is_equal_to(self.driver.title)

    @pytest.mark.parametrize("username,password,expected_error", DataSource.data_invalid_login)
    def test_invalid_login(self, username, password, expected_error):
        login = LoginPage(self.driver)
        login.enter_username(username)
        login.enter_password(password)

        self.driver.find_element(By.ID, "login-button").click()
        actual_error = self.driver.find_element(By.XPATH, "//p[contains(text(),'Invalid')]").text
        assert_that(actual_error).contains(expected_error)


class TestLoginUI(WebDriverWrapper):
    def test_title(self):
        print(self.driver)
        actual_title = self.driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)

    def test_app_description(self):
        actual_desc = self.driver.find_element(By.XPATH, "//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")

    def test_placeholder(self):
        actual_username_placeholder = self.driver.find_element(By.ID, "authUser").get_attribute("placeholder")
        actual_password_placeholder = self.driver.find_element(By.CSS_SELECTOR, "#clearPass").get_attribute(
            "placeholder")
        assert_that("Username").is_equal_to(actual_username_placeholder)
        assert_that("Password").is_equal_to(actual_password_placeholder)
