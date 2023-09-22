from helpers import BasePage


class FooterElement(BasePage):
    youtube_locator = '//a[@aria-label="youtube"]'
    instagram_Locator = '//a[@aria-label="instagram"]'
    facebook_locator = '//a[@aria-label="facebook"]'
    vk_locator = '//a[@aria-label="vk"]'
    telegram_locator = '//a[@aria-label="telegram"]'
    ok_locator = '//a[@aria-label="ok"]'
    about_us_locator = '//a[text()="О нас"]'
    store_addresses_locator = '//a[text()="Адреса магазинов"]'
    news_locator = '//a[text()="Новости"]'
    reviews_locator = '//a[text()="Статьи и обзоры"]'
    vacancy_locator = '//a[text()="Вакансии"]'
    contacts_page = '//a[text()="Контакты"]'

    def open(self):
        self.driver.get('https://5element.by/')

    def click_on_youtube(self):
        self.click_on(self.youtube_locator)

    def click_on_about_us_page(self):
        self.click_on(self.about_us_locator)

    def click_on_store_addresses_page(self):
        self.click_on(self.store_addresses_locator)

    def click_on_news_page(self):
        self.click_on(self.news_locator)

    def click_on_reviews_page(self):
        self.click_on(self.reviews_locator)

    def click_on_vacancy_page(self):
        self.click_on(self.vacancy_locator)

    def click_on_contacts_page(self):
        self.click_on(self.contacts_page)
