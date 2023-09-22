from helpers import BasePage


class PersonalCabinetPage(BasePage):
    cabinet_locator = '//div[text()="Личный кабинет"]'

    def open(self):
        self.driver.get('https://5element.by/cabinet')

    def assert_login_success(self):
        self.assert_element_is_displayed(self.cabinet_locator, True)

