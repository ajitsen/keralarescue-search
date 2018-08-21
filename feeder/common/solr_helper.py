import json
import os
import urllib.request
import pandas as pd

from feeder.common import config as config
from feeder.common.logger import log
from feeder.common.utils import my_sleep

RESCUE_COLLECTION = "krescue10"

CAMP_COLLECTION = "camp1"
VOLUNTEER_COLLECTION = "vol1"
RESOURCE_COLLECTION = "resource1"


def get_last_known_id_in_solr():
    url = config.SOLR_URL + "?fl=id&q=*:*&rows=1&sort=last_modified%20desc"
    req = urllib.request.Request(url, headers=config.get_req_header())
    response = urllib.request.urlopen(req).read()
    json_obj = json.loads(response.decode('utf-8'))
    if json_obj and isinstance(json_obj['response']['docs'], list):
        return json_obj['response']['docs'][0]['id']


def feed_csv_to_solr(collection, csv_file):
    lines = os.popen("wc -l " + csv_file + "| awk '{print $1}'").read()
    lines = int(lines.strip())
    log("===============")
    log("Json converted to CSV: " + csv_file + " lines: " + str(lines))
    if lines > 1:
        cmd = "/opt/solr/bin/post -c " + collection + " " + csv_file
        log("Feeding data to solr cmd:" + cmd)
        log(os.popen(cmd).readlines())
        my_sleep(10)


def get_data_frame_from_json(json_file, must_fields=None):
    with open(json_file) as fh:
        data_frame = pd.read_json(fh, dtype=False)
        if isinstance(must_fields, list) and len(must_fields) != 0:
            data_frame.dropna(subset=must_fields, inplace=True)
        return data_frame
