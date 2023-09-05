#  Создать минимум пять тестов для выбранного вами сайта
#  Добавить документацию к тестом, чтобы можно было понять о чем тест

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base import fill, wait_for_visible


"""
Locators
"""
login_button = '//*[@id="app"]/header/div[1]/div[1]/div/div/div[4]/a[2]/div/div[2]'
email = '//input[@name="login"]'
password = '//input[@type="password"]'
submit = '//*[@id="app"]/div[14]/div/div[2]/div[1]/form/div[4]'
login_locator = '//*[@id="app"]/header/div[1]/div[1]/div/div/div[4]/div[3]/a/span[2]'
logo = '//img[@src="/resources/images/logo_.svg"]'
discount = '//span[@class="h-discounts__text"]'
discount_locator = '//div[@class="section-heading__title"]'
current_city = '//*[@id="app"]/header/div[1]/div[1]/div/div/div[1]/div/div[2]'
new_city = '//*[@id="app"]/div[1]/div/div/div[2]/div/div[1]/div[2]'
final_city = "//div[contains(text(), 'Брест')]"
shops = "//a[contains(text(),'Магазины')]"
shop_map = "//button[contains(text(),'Карта')]"
yandex_map = '//ymaps[@class="ymaps-2-1-79-events-pane ymaps-2-1-79-user-selection-none"]'


def test_1(driver):
    """
    Log in on the 5element site
    """
    driver.get('https://5element.by/')
    enter_button = wait_for_visible(driver, login_button)
    enter_button.click()
    wait_for_visible(driver, email)
    fill(driver, email, 'bettertogo@gmail.com')
    wait_for_visible(driver, password)
    fill(driver, password, '123456')
    click_submit = wait_for_visible(driver, submit)
    click_submit.click()
    wait_for_visible(driver, login_locator)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, login_locator)))


def test_2(driver):
    """
    Check the presence of 5element logo on the main page"
    """
    driver.get('https://5element.by/')
    locator_logo = wait_for_visible(driver, logo)
    assert WebDriverWait(driver, 10).until(EC.element_to_be_clickable(locator_logo))


def test_3(driver):
    """
    Check the sales page
    """
    driver.get('https://5element.by/')
    sales = wait_for_visible(driver, discount)
    sales.click()
    wait_for_visible(driver, discount_locator)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, discount_locator)))


def test_4(driver):
    """
   Check possibility to change current city of a client
    """
    driver.get('https://5element.by/')
    city = wait_for_visible(driver, current_city)
    city.click()
    change_city = wait_for_visible(driver, new_city)
    change_city.click()
    wait_for_visible(driver, final_city)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, final_city)))


def test_5(driver):
    """
    Check the presence of a map with shops
    """
    driver.get('https://5element.by/')
    shop_list = wait_for_visible(driver, shops)
    shop_list.click()
    view_shop_map = wait_for_visible(driver, shop_map)
    view_shop_map.click()
    wait_for_visible(driver, yandex_map)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, yandex_map)))
