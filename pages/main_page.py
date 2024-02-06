class MainPage:
    def __init__(self, driver):
        self.__driver = driver

    @property
    def get_main_title(self):
        return self.driver.title