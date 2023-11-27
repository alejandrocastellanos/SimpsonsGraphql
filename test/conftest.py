import asyncio
import uvloop

from graphene.test import Client
from pytest import fixture


from simpsons.api import schema


@fixture(scope='session')
def event_loop():
    loop = uvloop.new_event_loop()
    asyncio.set_event_loop(loop=loop)
    yield loop
    loop.close()


@fixture
def graph_client(event_loop):
    return Client(schema=schema)


@fixture
def graphql_context_fixture():
    class Request:
        client = ('127.0.0.1', '60000')

    return {'request': Request()}
