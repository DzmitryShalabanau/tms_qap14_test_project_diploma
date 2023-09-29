import allure

from helpers import BasePage


class IframePage(BasePage):

    iframe_text = '//*[@id="tinymce"]/p'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open iframe page')
    def open(self):
        self.driver.get('http://the-internet.herokuapp.com/iframe')

    @allure.step('Switch for work with iframe')
    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    @allure.step('Fill text in iframe')
    def text_fill(self):
        self.fill(self.iframe_text, 'Dzmitry Shalabanau')

    @allure.step('Check if text in iframe is correct')
    def assert_iframe(self):
        self.assert_text_in_element(self.iframe_text, 'Dzmitry Shalabanau')




