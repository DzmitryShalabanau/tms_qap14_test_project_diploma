from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

WAIT_UNTIL = 5


def check_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()


def uncheck_checkbox(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    if element.is_selected():
        element.click()
    else:
        print("The element is already selected")


def scroll_down(driver):
    driver.execute_script("window.scrollTo(0, window.innerHeight);")


def select_radio_button(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    element.click()


def dropdown_select(driver, locator, value):
    element = Select(driver.find_element(By.XPATH, locator))
    element.select_by_value(value)


def get_input_text(driver, locator, text):
    element = driver.find_element(By.XPATH, locator)
    element.clear()
    element.send_keys(text)
    element.get_attribute(text)


def get_attribute(driver, locator, attribute_name):
    element = driver.find_element(By.XPATH, locator)
    element.get_attribute(attribute_name)


def wait_for_element_is_displayed(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    time.sleep(5)
    if element.is_displayed():
        pass
    else:
        return print(f"Element {locator} is  not displayed")


def wait_for_element_is_enabled(driver, locator):
    element = driver.find_element(By.XPATH, locator)
    time.sleep(5)
    if element.is_enabled():
        pass
    else:
        return print(f"Element {locator} is  not enabled")