import allure

from services.pokeapi import PokeApiService


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur ID check')
@allure.step('Check ID of Bulbasaur')
def test_pokemon_id():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["id"] == 1, "ID test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur name check')
@allure.step('Check name of Bulbasaur')
def test_pokemon_name():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["name"] == "bulbasaur", "Name test failed"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur height check')
@allure.step('Check height of Bulbasaur')
def test_pokemon_height():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["height"] == 7, "Height test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur weight check')
@allure.step('Check weight of Bulbasaur')
def test_pokemon_weight():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["weight"] == 69, "Weight test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur base experience check')
@allure.step('Check base experience of Bulbasaur')
def test_pokemon_base_experience():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["base_experience"] == 64, "Base test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur held items check')
@allure.step('Check held items of Bulbasaur')
def test_pokemon_held_items():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["held_items"] == [], "Held Items  test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur default check')
@allure.step('Check if Bulbasaur is default')
def test_if_pokemon_is_default():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["is_default"] == True, "Default  test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur order check')
@allure.step('Check order of Bulbasaur')
def test_pokemon_order():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["order"] == 1, "Order  test failed!"


@allure.suite('Bulbasaur tests')
@allure.title('Bulbasaur order check')
@allure.step('Check order of Bulbasaur')
def test_pokemon_past_types():
    pokeapi_service = PokeApiService()
    response = pokeapi_service.get_pokemon_info_by_name('bulbasaur')
    assert response["past_types"] == [], "Past test failed!"

