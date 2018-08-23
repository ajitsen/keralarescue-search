from unittest import TestCase

from common.config import ELASTIC_CAMP_INDEX
from common.elastic_helper import get_elastic_client, get_count_match_all


class TestElasticHelper_all(TestCase):
    def test_match_all_request(self):
        client = get_elastic_client()
        results = get_count_match_all(client, 'requests_import')
        print(results)
        self.assertTrue(results['hits']['total'] > 1000)

    def test_match_all_camp(self):
        client = get_elastic_client()
        results = get_count_match_all(client, ELASTIC_CAMP_INDEX)
        print(results)
        self.assertTrue(results['hits']['total'] > 2)
