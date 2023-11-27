import graphene

from graphene import ObjectType


class QuotesType(ObjectType):
    image = graphene.String()
    quote = graphene.String()
