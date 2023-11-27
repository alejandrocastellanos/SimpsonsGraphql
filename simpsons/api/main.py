from fastapi import FastAPI
from graphene import Schema
from starlette.middleware.cors import CORSMiddleware
from starlette_graphene3 import GraphQLApp

from simpsons.query.query import Query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)

schema = Schema(query=Query)

app.add_route("/graphql", GraphQLApp(schema=schema))
