from unittest import TestCase

from common.elastic_helper import get_elastic_client, get_count_match_all


class TestElasticHelper_all(TestCase):
    def test_match_all(self):
        client = get_elastic_client()
        results = get_count_match_all(client, 'requests_import')
        print(results)
        self.assertTrue(results['hits']['total'] > 1000)
