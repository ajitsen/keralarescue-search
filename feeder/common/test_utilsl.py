import os
from unittest import TestCase

from common.utils import get_data_from_url, get_md5


class TestGet_data_from_url(TestCase):
    def test_get_data_from_url(self):
        url = 'https://google.com'
        self.assertTrue('<!doctype html>' in get_data_from_url(url))

        self.assertTrue('<!doctype html>' in get_data_from_url(url, cache=True))
        cache_file_name = "/tmp/" + get_md5(url)
        self.assertTrue(len(os.popen("wc -l " + cache_file_name).read()) > 10)

