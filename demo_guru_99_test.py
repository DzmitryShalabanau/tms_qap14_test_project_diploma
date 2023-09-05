
# Задание 2
# 1. Открыть сайт http://demo.guru99.com/test/newtours/register.php
# 2. Заполнить все поля
# 3. Нажать кнопку Submit
# 4. Проверить, что отображается правильно имя и фамилия
# 5.Проверить, что отображается правильно username



from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from base import fill_2, wait_for_visible

first_name = '[name="firstName"]'
last_name = '[name="lastName"]'
phone = '[name="phone"]'
mail = '[id="userName"]'
address = '[name="address1"]'
city = '[name="city"]'
province = '[name="state"]'
postcode = '[name="postalCode"]'
country = '[name="country"]'
user_name = '[name="email"]'
password1 = '[name="password"]'
confirm_password = '[name="confirmPassword"]'
submit = '[name="submit"]'
name_check = "//b[contains(text(),'Dear Ben')]"
nick_name_check = "//b[contains(text(),'dronedoom')]"


def test_1(driver):

    driver.get('http://demo.guru99.com/test/newtours/register.php')
    fill_2(driver, first_name, 'Ben')
    fill_2(driver, last_name, "Johnson")
    fill_2(driver, phone, '+375441111111')
    fill_2(driver, mail, 'bettertogo@gmail.com')
    fill_2(driver, address, 'Shugaeva 13/138')
    fill_2(driver, city, 'Minsk')
    fill_2(driver, province, 'Uruchcha')
    fill_2(driver, postcode, '220141')
    dd_country = Select(driver.find_element(By.CSS_SELECTOR, country))
    dd_country.select_by_value('BELARUS')
    fill_2(driver, user_name, 'dronedoom')
    fill_2(driver, password1, '12345678')
    fill_2(driver, confirm_password, '12345678')
    register = driver.find_element(By.CSS_SELECTOR, submit)
    register.click()
    result = wait_for_visible(driver, name_check)
    print(result.text)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, name_check)))


def test_2(driver):

    driver.get('http://demo.guru99.com/test/newtours/register.php')
    fill_2(driver, first_name, 'Ben')
    fill_2(driver, last_name, "Johnson")
    fill_2(driver, phone, '+375441111111')
    fill_2(driver, mail, 'bettertogo@gmail.com')
    fill_2(driver, address, 'Shugaeva 13/138')
    fill_2(driver, city, 'Minsk')
    fill_2(driver, province, 'Uruchcha')
    fill_2(driver, postcode, '220141')
    dd_country = Select(driver.find_element(By.CSS_SELECTOR, country))
    dd_country.select_by_value('BELARUS')
    fill_2(driver, user_name, 'dronedoom')
    fill_2(driver, password1, '12345678')
    fill_2(driver, confirm_password, '12345678')
    register = driver.find_element(By.CSS_SELECTOR, submit)
    register.click()
    result = wait_for_visible(driver, nick_name_check)
    print(result.text)
    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, nick_name_check)))
