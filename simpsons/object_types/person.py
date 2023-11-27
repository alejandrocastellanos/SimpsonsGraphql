import graphene

from graphene import ObjectType


class PersonType(ObjectType):
    name = graphene.String()
    story = graphene.String()
    image = graphene.String()
    gender = graphene.String()
    status = graphene.String()
    occupation = graphene.String()
