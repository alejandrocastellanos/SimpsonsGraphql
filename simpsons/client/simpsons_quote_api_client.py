import httpx


class SimpsonsQuotesApiClient:

    url = 'https://thesimpsonsquoteapi.glitch.me/quotes'

    async def random_quote(self):
        request = await self.request(self.url)
        if request.status_code == 200:
            return request.json()
        else:
            return {'error': request.status_code}

    async def quote_by_character(self, name: str):
        url = f'{self.url}?count=5&character={name}'
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
