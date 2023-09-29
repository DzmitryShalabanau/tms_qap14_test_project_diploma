from helpers import BasePage


class ActionsPage(BasePage):
    discount_locator = '//*[@id="app"]/main/div[2]/div/div/div[1]/div[1]'

    def open(self):
        self.driver.get('https://5element.by/actions')

    def assert_sales_page(self):
        self.assert_element_is_displayed(self.discount_locator, True)


