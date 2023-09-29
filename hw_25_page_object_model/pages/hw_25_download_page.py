import allure

from helpers import BasePage


class DownloadPage(BasePage):
    url = 'https://the-internet.herokuapp.com/download/LambdaTest.txt'
    file_path = 'E:\\hw_25_page_object_model\\tests\\LambdaTest.txt'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Open download page')
    def open(self):
        self.driver.get('http://the-internet.herokuapp.com/download')

    @allure.step('Download file')
    def download_file(self):
        self.pump(self.url, 'LambdaTest.txt')

    @allure.step('Check if downloaded file is in directory')
    def assert_if_file_exists(self):
        self.check_file(self.file_path, True)







