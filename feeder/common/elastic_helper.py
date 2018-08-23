from elasticsearch import Elasticsearch
from pip._vendor import certifi

from common.config import ELASTIC_HOST
import cred

'''
Low Level Elastic Client https://elasticsearch-py.readthedocs.io/en/master/
High Level Elastic Client https://elasticsearch-dsl.readthedocs.io/en/latest/
'''


def get_elastic_client():
    return Elasticsearch(
        [ELASTIC_HOST],
        http_auth=(cred.elastic['user'], cred.elastic['password']),
        scheme="https",
        port=443,
        ca_certs=certifi.where()
    )


def get_count_match_all(client, index):
    result = client.search(
        index=index,
        body={"query": {"match_all": {}}},
        size=0
    )
    return result


def create_index(client, index, mapping_settings):
    # ignore 400 cause by IndexAlreadyExistsException when creating an index
    return client.indices.create(index=index, body=mapping_settings, ignore=400)






