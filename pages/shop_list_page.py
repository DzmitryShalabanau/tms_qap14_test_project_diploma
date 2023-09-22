from helpers import BasePage


class ShopListPage(BasePage):
    shop_map = "//button[contains(text(),'Карта')]"
    yandex_map = '//*[@id="app"]/main/div[2]/div/div/div[3]'

    def open(self):
        self.driver.get('https://5element.by/shops')

    def click_on_shop_map(self):
        self.click_on(self.shop_map)

    def assert_shop_map(self):
        self.assert_element_is_displayed(self.yandex_map, True)


