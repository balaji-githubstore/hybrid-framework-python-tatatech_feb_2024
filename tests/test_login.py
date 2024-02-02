from selenium import webdriver
from assertpy import assert_that
from selenium.webdriver.common.by import By


class TestLoginUI:
    def test_title(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://demo.openemr.io/b/openemr")
        actual_title = driver.title
        assert_that("OpenEMR Login").is_equal_to(actual_title)

    def test_app_description(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get("https://demo.openemr.io/b/openemr")
        actual_desc= driver.find_element(By.XPATH,"//p[contains(text(),'most')]").text
        assert_that(actual_desc).contains("Electronic Health Record and Medical Practice Management")
