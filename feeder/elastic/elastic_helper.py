from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch import helpers
from pip._vendor import certifi

import cred
from common.config import ELASTIC_HOST

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


# https://elasticsearch-dsl.readthedocs.io/en/latest/
def get_count_match_data_type(client, index, data_type, count):
    s = Search(using=client, index=index).query("match", data_type=data_type)
    return len(s[:count].execute())


def create_index(client, index, mapping_settings):
    # ignore 400 cause by IndexAlreadyExistsException when creating an index
    return client.indices.create(index=index, body=mapping_settings, ignore=400)


def get_bulk_index_json(index, doc_id):
    # return '"_index" : "'+index+'", "_type" : "_doc", "_id" : "'+doc_id+'" '
    return '{ "index" : { "_index" : "'+index+'", "_type" : "_doc", "_id" : "'+doc_id+'" } }'


def feed_bulk_to_elastic(bulk_actions):
    client = get_elastic_client()
    result = helpers.bulk(client, bulk_actions)
    print(result)

# PUT /requests_import
# {
#   "settings": {
#     "analysis": {
#       "filter": {
#         "my_synonym_filter": {
#           "type": "synonym",
#           "synonyms": [
#             "tvm,Thiruvananthapuram",
#             "ptm,Pathanamthitta",
#             "alp,Alappuzha",
#             "ktm,Kottayam",
#             "idk,Idukki",
#             "mpm,Malappuram",
#             "koz,Kozhikode",
#             "wnd,Wayanad",
#             "knr,Kannur",
#             "ksr,Kasaragod",
#             "pkd,Palakkad",
#             "tcr,Thrissur",
#             "ekm,Ernakulam",
#             "kol,Kollam"
#           ]
#         }
#       },
#       "analyzer": {
#         "my_synonyms": {
#           "tokenizer": "standard",
#           "filter": [
#             "lowercase",
#             "my_synonym_filter"
#           ]
#         }
#       }
#     }
#   }
# }


