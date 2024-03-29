from typing import Tuple

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""This module contains all the webdriver keywords"""

class WebDriverKeywords:
    def __init__(self, driver):
        self.__driver = driver
        self.__wait = WebDriverWait(driver, 30)

    def type_on_element(self, locator: Tuple[str, str], text:str):
        self.__wait.until(
            expected_conditions.visibility_of_element_located(locator)).send_keys(text)

    def click_on_element(self, locator: Tuple[str, str]):
        self.__wait.until(
            expected_conditions.visibility_of_element_located(locator)).click()

    def get_text_from_element(self, locator: Tuple[str, str]):
        return self.__wait.until(
            expected_conditions.visibility_of_element_located(locator)).text

    def get_attribute_from_element(self, locator: Tuple[str, str],attribute_name: str):
        return self.__wait.until(
            expected_conditions.visibility_of_element_located(locator)).get_attribute(attribute_name)

    #switch_tab_by_title()
    #get_text_and_handle_alert()