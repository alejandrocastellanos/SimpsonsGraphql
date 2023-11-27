from translate import Translator

from simpsons.client.simpsons_api_client import SimpsonsApiClient
from simpsons.client.simpsons_quote_api_client import SimpsonsQuotesApiClient


class SimpsonsController:

    __slots__ = (
        '_instance_simpsons_client',
        '_instance_simpsons_quotes_client'
    )

    def __init__(self):
        self._instance_simpsons_client = SimpsonsApiClient()
        self._instance_simpsons_quotes_client = SimpsonsQuotesApiClient()

    async def character_list(self, page, limit):
        response = await self._instance_simpsons_client.character_list(page=page, limit=limit)
        return [self.dict_translate(data) for data in response.get('docs')]

    async def get_character(self, name):
        response = await self._instance_simpsons_client.get_character(name)
        return [self.dict_translate(data) for data in response.get('result')]

    async def random_quote(self):
        response = await self._instance_simpsons_quotes_client.random_quote()
        return [{
            'image': response[0].get('image'),
            'quote': self.translate(response[0].get('quote'))
        }]

    async def random_quote_by_character(self, name):
        response = await self._instance_simpsons_quotes_client.quote_by_character(name)
        data_result = []
        for data in response:
            data_result.append(
                {
                    'image': data.get('image'),
                    'quote': self.translate(data.get('quote'))
                }
            )
        return data_result

    @staticmethod
    def dict_translate(data_result: dict):
        translate = {
            '_id': 'id',
            'Nombre': 'name',
            'Historia': 'story',
            'Imagen': 'image',
            'Genero': 'gender',
            'Estado': 'status',
            'Ocupacion': 'occupation'
        }
        return {translate.get(key, key): value for key, value in data_result.items()}

    @staticmethod
    def translate(text):
        translator = Translator(to_lang="es")
        return translator.translate(text)
