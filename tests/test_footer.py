from elements import FooterElement


def test_check_about_us_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_about_us_page()
    footer.assert_actual_url('https://5element.by/company')


def test_check_store_addresses_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_store_addresses_page()
    footer.assert_actual_url('https://5element.by/shops')


def test_check_news_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_news_page()
    footer.assert_actual_url('https://5element.by/news')


def test_check_reviews_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_reviews_page()
    footer.assert_actual_url('https://5element.by/article/131295-poleznye-stati')


def test_check_vacancy_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_vacancy_page()
    footer.assert_actual_url('https://5element.by/company/vacancy')


def test_contacts_page(driver):
    footer = FooterElement(driver)
    footer.open()
    footer.click_on_contacts_page()
    footer.assert_actual_url('https://5element.by/company/contacts')









