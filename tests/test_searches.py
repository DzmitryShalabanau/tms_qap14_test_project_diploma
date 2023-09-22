import pytest

from elements import HeaderElement
from pages.actions_page import ActionsPage
from pages.cabinet_page import PersonalCabinetPage
from pages.shop_list_page import ShopListPage


def test_log_in_fifth_element_site(driver):
    header = HeaderElement(driver)
    cabinet = PersonalCabinetPage(driver)
    header.open()
    header.click_on_login_button()
    header.enter_user_data()
    header.click_on_submit_button()
    header.click_on_personal_account()
    cabinet.assert_login_success()


def test_check_sales_page(driver):
    header = HeaderElement(driver)
    actions = ActionsPage(driver)
    header.open()
    header.click_on_sales()
    actions.assert_sales_page()


def test_shops_map(driver):
    header = HeaderElement(driver)
    shop_list = ShopListPage(driver)
    header.open()
    header.click_on_shop_list()
    shop_list.click_on_shop_map()
    shop_list.assert_shop_map()










