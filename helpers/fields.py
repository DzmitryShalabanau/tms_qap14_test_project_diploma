from base import BasePage


class FieldsWebElement(BasePage):
    def __init__(self, driver, WAIT_UNTIL=5):
        super().__init__(driver, WAIT_UNTIL)
        self.driver = driver
        self.WAIT_UNTIL = WAIT_UNTIL

    def fill(self, locator, text):
        element = self.wait_for_visible(locator)
        element.clear()
        element.sendKeys(text)

    def clear(self, locator):
        element = self.wait_for_visible(locator)
        element.clear()
