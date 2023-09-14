from selenium.webdriver.common.by import By

photo_locator = '[class="gs-c-promo-image gs-u-mb gs-u-mb0@xs gs-u-float-right@m gel-2/3@m gs-u-display-block"]'
bbc_locator = '[width="112"]'
sport_locator = 'nav[class="orbit-header-links international"] li[class="orb-nav-sport"]'
home_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li:first-of-type > a'
climate_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li:nth-of-type(3) > a'
world_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li:nth-of-type(5) > a'
business_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li:nth-of-type(7) > a'
science_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li:nth-of-type(9) > a'
ent_locator = 'div:nth-of-type(2) > div > div:first-of-type > nav > ul > li > a'
world_news_locator = '#orb-modules > header > div:nth-of-type(2) > div > div:first-of-type > nav > ul > li > a'


def test_1(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, photo_locator)
    assert element.is_displayed() == True


def test_2(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, bbc_locator)
    assert element.is_displayed() == True


def test_3(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, sport_locator)
    assert element.is_displayed() == True


def test_4(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, home_locator)
    assert element.is_displayed() == True


def test_5(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, climate_locator)
    assert element.is_displayed() == True


def test_6(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, world_locator)
    assert element.is_displayed() == True


def test_7(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, business_locator)
    assert element.is_displayed() == True


def test_8(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, science_locator)
    assert element.is_displayed() == True


def test_9(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, ent_locator)
    assert element.is_displayed() == True


def test_10(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.CSS_SELECTOR, world_news_locator)
    assert element.is_displayed() == True


