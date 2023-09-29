import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select
import urllib.request
import os


class BasePage:
    def __init__(self, driver, WAIT_UNTIL=5):
        self.urllib = urllib
        self.os = os
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    @allure.step('Find element on page')
    def wait_for_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.WAIT_UNTIL).until(EC.element_to_be_clickable((By.XPATH, locator)))
        except WebDriverException:
            assert False, f"Element {locator} not clickable"

    @allure.step('Click on element')
    def click_on(self, locator):
        element = self.wait_for_visible(locator)
        element.click()

    @allure.step('Hard Click on element')
    def hard_click(self, locator):
        element = self.driver.find_element(By.XPATH, locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Enter url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Fill fields')
    def fill(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Clear fields')
    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()

    @allure.step('Check for text presence in element')
    def assert_text_in_element(self, locator, expected_result):
        element = self.wait_for_visible(locator)
        assert element.text == expected_result, "Text not the same"

    @allure.step('Select value of element')
    def select_by_value(self, select, value):
        element = self.wait_for_visible(select)
        select = Select(element)
        select.select_by_value(value)

    @allure.step('Switch to iframe')
    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    @allure.step('Set display none')
    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display", arguments[1])', element, 'none')

    @allure.step('Fill text in alert')
    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Dzmitry")
        alert.accept()

    @allure.step('Open new window')
    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    @allure.step('Check the presence of value in element')
    def assert_value_in_element_attribute(self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        assert value == expected_result, "Attribute value not the same"

    @allure.step('Check if url is correct')
    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    @allure.step('Add cookie')
    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    @allure.step('Delete cookies')
    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()

    @allure.step('Check if element is displayed')
    def assert_element_is_displayed(self, locator, expected_result):
        element = self.driver.find_element(By.XPATH, locator)
        assert element.is_displayed() == expected_result, "Element is not displayed"

    @allure.step('Download file')
    def pump(self, url, filename):
        response = self.urllib.request.urlopen(url)
        file = open(filename, 'wb')
        file.write(response.read())
        file.close()

    @allure.step('Check presence of file in directory')
    def check_file(self, file_path, expected_result):
        check_file = self.os.path.isfile(file_path)
        assert check_file == expected_result, "File does not exist"
