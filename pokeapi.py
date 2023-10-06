import allure

from helpers.base_service import BaseService


class PokeApiService(BaseService):

    @allure.step('Get {name} info')
    def get_pokemon_info_by_name(self, name):
        response = self.get(f'{name}')
        return response
