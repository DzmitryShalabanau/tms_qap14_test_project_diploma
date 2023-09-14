from selenium.webdriver.common.by import By

photo_locator = '//div[@class="gs-c-promo-image gs-u-mb gs-u-mb0@xs gs-u-float-right@m gel-2/3@m gs-u-display-block"]'
bbc_locator = '//a[@id="homepage-link"]'
sport_locator = '//*[@id="orb-header"]/div/nav[2]/ul/li[3]'
home_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[1]/a'
climate_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[3]/a'
world_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[5]/a'
business_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[7]/a'
science_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[9]/a'
ent_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[10]/a'
world_news_locator = '//*[@id="orb-modules"]/header/div[2]/div/div[1]/nav/ul/li[12]/a'


def test_1(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, photo_locator)
    assert element.is_displayed() == True


def test_2(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, bbc_locator)
    assert element.is_displayed() == True


def test_3(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, sport_locator)
    assert element.is_displayed() == True


def test_4(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, home_locator)
    assert element.is_displayed() == True


def test_5(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, climate_locator)
    assert element.is_displayed() == True


def test_6(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, world_locator)
    assert element.is_displayed() == True


def test_7(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, business_locator)
    assert element.is_displayed() == True


def test_8(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, science_locator)
    assert element.is_displayed() == True


def test_9(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, ent_locator)
    assert element.is_displayed() == True


def test_10(driver):
    driver.get('https://www.bbc.com/news')
    element = driver.find_element(By.XPATH, world_news_locator)
    assert element.is_displayed() == True

