from unittest import TestCase

import common.config as config
from elastic.elastic_helper import get_elastic_client, get_count_match_all, get_count_match_data_type


class TestElasticHelper_all(TestCase):
    def test_match_all_request(self):
        client = get_elastic_client()
        results = get_count_match_all(client, 'requests_import')
        print(results)
        self.assertTrue(results['hits']['total'] > 1000)

    def test_match_all_camp(self):
        client = get_elastic_client()
        count = 2
        results = get_count_match_data_type(client, config.ELASTIC_INDEX, config.ELASTIC_CAMP_TYPE, count)
        self.assertTrue(results == count)

    def test_match_all_demand(self):
        client = get_elastic_client()
        results = get_count_match_all(client, config.ELASTIC_DEMAND_TYPE)
        print(results)
        self.assertTrue(results['hits']['total'] > 2)
