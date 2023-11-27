import httpx


class SimpsonsApiClient:

    url = 'https://apisimpsons.fly.dev/api'

    async def character_list(self, page: int, limit: int):
        url = f'{self.url}/personajes?limit={limit}&page={page}'
        request = await self.request(url)
        if request.status_code == 200:
            return request.json()
        else:
            return {'error': request.status_code}

    async def get_character(self, name: str):
        url = f'{self.url}/personajes/find/{name}'
        request = await self.request(url)
        if request.status_code == 200:
            return request.json()
        else:
            return {'error': request.status_code}

    @staticmethod
    async def request(url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
        return response
