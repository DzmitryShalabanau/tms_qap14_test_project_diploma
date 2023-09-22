from elements import FooterElement, HeaderElement
from helpers import BasePage


class MainPage(BasePage, FooterElement, HeaderElement):
    def open(self):
        self.driver.get('https://5element.by/')
