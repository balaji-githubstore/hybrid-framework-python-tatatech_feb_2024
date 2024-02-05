from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.__driver=driver

    def enter_username(self,username):
        self.__driver.find_element(By.ID, "authUser").send_keys(username)

    def enter_password(self,password):
        self.__driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(password)

    #click on login

    #get_error_message()