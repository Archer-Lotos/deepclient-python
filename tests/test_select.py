import unittest
import asyncio
import os
from dotenv import load_dotenv
from deepclient import DeepClient, DeepClientOptions
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


class TestDeepClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        load_dotenv()
        transport = AIOHTTPTransport(
            url=os.getenv('URL_GQL'),
            headers={'Authorization': 'Bearer %s' % (os.getenv('BEARER_TOKEN'))}
        )
        client = Client(transport=transport, fetch_schema_from_transport=True)

        self.options = DeepClientOptions(gql_client=client)
        self.client = DeepClient(self.options)

    async def testSelect(self):
        assert (await self.client.select(1))['data'][0] == {'id': 1, 'type_id': 1, 'from_id': 8, 'to_id': 8,
                                                            'value': None}
        assert (await self.client.select({"id": 1}))['data'][0] == {'id': 1, 'type_id': 1, 'from_id': 8, 'to_id': 8,
                                                                    'value': None}
        assert (await self.client.select({"id": {"_eq": 1}}))['data'][0] == {'id': 1, 'type_id': 1, 'from_id': 8,
                                                                             'to_id': 8, 'value': None}