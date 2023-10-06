import allure
import requests


class BaseService:
    HOST = 'https://pokeapi.co/api/v2/pokemon/'

    @allure.step('URL: {url}')
    def get(self, url, code=200):
        response = requests.get(self.HOST + url)
        assert response.status_code == code, f'Have code = {response.status_code}'
        print(response.json)
        return response.json()

    @allure.step('URL: {url}')
    def post(self, url, body, code=200):
        response = requests.post(self.HOST + url, data=body)
        assert response.status_code == code
        print(response.json)
        return response.json()

