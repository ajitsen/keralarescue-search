import hashlib
import json
import time
import urllib.request

from feeder.common import config as config
from feeder.common.logger import log
from feeder.common.my_pandas import pandas_read_tsv_str


def my_sleep(sec):
    from feeder.common.logger import log
    if sec < 2:
        log("Sleeping. < 2sec")
        time.sleep(sec)
        return
    for i in range(sec):
        log("Sleeping...")
        time.sleep(1)

def get_md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def get_data_from_url(url, cache=False):
    from feeder.common.logger import log

    if not cache:
        log("Getting data from " + url)
        return _get_data_from_url(url)

    cache_file_name = "/tmp/" + get_md5(url)
    log("Using cache " + cache_file_name)
    try:
        fh = open(cache_file_name, "r")
        cache_str = fh.read()
        fh.close()
        return cache_str
    except IOError:
        log("Cahe Miss - Failed to read " + cache_file_name, error=True)
        log("Getting data from " + url)
        string = _get_data_from_url(url)
        with open(cache_file_name, "w") as fw:
            fw.write(string)
            fw.close()
        return string


def _get_data_from_url(url):
    req = urllib.request.Request(url, headers=config.get_req_header())
    response = urllib.request.urlopen(req).read()
    string = response.decode('utf-8')
    return string


def load_sheet_tsv_as_panda_df(sheet_url):
    tsv_str = get_data_from_url(sheet_url, cache=True)
    dataf = pandas_read_tsv_str(tsv_str)
    log("Loaded data from ")
    log(dataf.shape)
    log(dataf.columns)
    return dataf


'''
Saves given url, save json array to file
return file name on success
'''
def save_data_json(url, cache=False):
    log("Downloading " + url)
    json_file = "/tmp/" + get_md5(url) + ".json"
    json_obj = json.loads(get_data_from_url(url, cache=cache))
    with open(json_file, "w") as fh:
        fh.write(json.dumps(json_obj))
        fh.close()
        return json_file
