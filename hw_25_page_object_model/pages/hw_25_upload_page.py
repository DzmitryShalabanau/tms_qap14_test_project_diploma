import allure

from helpers import BasePage


class UploadPage(BasePage):

    upload_locator = '//input[@id="file-upload"]'
    upload_button_locator = '//input[@value="Upload"]'
    upload_result_locator = '//div[@id="uploaded-files"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open upload page')
    def open(self):
        self.driver.get('http://the-internet.herokuapp.com/upload')

    @allure.step('Upload file')
    def add_sample_file(self):
        self.fill(self.upload_locator, 'C:\\Users\\dronedoom\\sample.txt')

    @allure.step('Check if file is uploaded')
    def assert_upload(self):
        self.click_on(self.upload_button_locator)
        self.assert_text_in_element(self.upload_result_locator, 'sample.txt')

