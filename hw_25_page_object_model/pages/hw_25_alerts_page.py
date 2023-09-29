import allure

from helpers import BasePage


class AlertsPage(BasePage):

    click_for_js_prompt_button = '//button[@onclick="jsPrompt()"]'
    alert_result = '//p[@id="result"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open alerts Page')
    def open(self):
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')

    @allure.step('Click on alert')
    def click_on_js_prompt_button(self):
        self.click_on(self.click_for_js_prompt_button)

    @allure.step('Switch to alert')
    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Dzmitry")
        alert.accept()

    @allure.step('Check if text in alert is right')
    def assert_prompt_alert(self):
        self.assert_text_in_element(self.alert_result, 'You entered: Dzmitry')
