from helpers import BasePage
from helpers.fields import FieldsWebElement


class ObjectPage(BasePage):
    delete = FieldsWebElement('xpath')

    def open(self):
        self.driver.get('https://5element.by/')

