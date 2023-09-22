from helpers import BasePage


class HeaderElement(BasePage):
    logo_locator = '//img[@src="/resources/images/logo_.svg"]'
    login_button = '//*[@id="app"]/header/div[1]/div[1]/div/div/div[4]/a[2]/div/div[2]'
    email = '//input[@name="login"]'
    password = '//input[@type="password"]'
    submit = '//*[@id="app"]/div[14]/div/div[2]/div[1]/form/div[4]'
    account_locator = '//*[@id="app"]/header/div[1]/div[1]/div/div/div[4]/div[3]'
    discount = '//span[@class="h-discounts__text"]'
    current_city = '//div[text()="Минск"]'
    new_city = '//div[text()="Брест"]'
    final_city = '//div[text()="Брест"]'
    shops = '//a[text()="Магазины"]'
    search_form = '//form[@class="h-search__form"]'
    search_form_for_fill = '//*[@id="app"]/header/div[1]/div[2]/div/div[1]/div[2]/div[1]/form/input[3]'
    search_button = '//*[@id="app"]/header/div[1]/div[2]/div/div[1]/div[2]/div[1]/form/div/button[2]'
    search_result = '//div[text()="Результаты поиска «notebook»"]'

    def open(self):
        self.driver.get('https://5element.by/')

    def find_fifth_element_logo(self):
        self.wait_for_visible(self.logo_locator)

    def assert_fifth_element_logo(self):
        self.assert_element_is_displayed(self.logo_locator, True)

    def click_on_login_button(self):
        self.click_on(self.login_button)

    def enter_user_data(self):
        self.wait_for_visible(self.email)
        self.fill(self.email, 'bettertogo@gmail.com')
        self.wait_for_visible(self.password)
        self.fill(self.password, '123456')

    def click_on_submit_button(self):
        self.click_on(self.submit)

    def click_on_personal_account(self):
        self.click_on(self.account_locator)

    def click_on_sales(self):
        self.click_on(self.discount)

    def click_on_current_city(self):
        self.click_on(self.current_city)

    def change_city(self):
        self.click_on(self.new_city)

    def assert_changed_city(self):
        self.assert_element_is_displayed(self.final_city, True)

    def click_on_shop_list(self):
        self.click_on(self.shops)

    def click_on_search_form(self):
        self.click_on(self.search_form)

    def fill_search_form(self):
        self.wait_for_visible(self.search_form_for_fill)
        self.fill(self.search_form_for_fill, 'notebooks')

    def click_on_search_button(self):
        self.click_on(self.search_button)

    def assert_search_result(self):
        self.assert_element_is_displayed(self.search_result, True)








