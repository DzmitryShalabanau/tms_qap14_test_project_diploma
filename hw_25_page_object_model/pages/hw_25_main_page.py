import allure

from helpers import BasePage


class MainPage(BasePage):
    javascript_alerts_button = '//a[@href="/javascript_alerts"]'
    new_window_url = 'https://the-internet.herokuapp.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open main page')
    def open(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    @allure.step('Open switch to new window')
    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    @allure.step('Check new window url')
    def assert_new_window(self):
        self.assert_actual_url(self.new_window_url)



