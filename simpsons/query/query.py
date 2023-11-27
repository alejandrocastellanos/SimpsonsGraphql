from graphene import ObjectType, List, String, Int

from simpsons.controller.simpsons_controller import SimpsonsController
from simpsons.object_types.person import PersonType
from simpsons.object_types.quotes import QuotesType

simpsons_controller = SimpsonsController()


class Query(ObjectType):

    character_description = List(PersonType, name=String())
    character_list = List(PersonType, page=Int(), limit=Int())
    random_famous_quotes = List(QuotesType)
    random_famous_quotes_by_character = List(QuotesType, name=String())

    @staticmethod
    async def resolve_character_description(_, info, name):
        return await simpsons_controller.get_character(name)

    @staticmethod
    async def resolve_character_list(_, info, page, limit):
        return await simpsons_controller.character_list(page, limit)
    
    @staticmethod
    async def resolve_random_famous_quotes(_, info):
        response = await simpsons_controller.random_quote()
        return response

    @staticmethod
    async def resolve_random_famous_quotes_by_character(_, info, name):
        response = await simpsons_controller.random_quote_by_character(name)
        return response
