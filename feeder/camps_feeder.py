import pandas as pd
from slugify import slugify

from feeder.camp_transformer import process_camps_feed
from feeder.common.config import CAMP_SHEET, RESOURCE_SHEET, VOLUNTEER_SHEET
from feeder.common.logger import log
from feeder.common.solr_helper import CAMP_COLLECTION, feed_csv_to_solr, VOLUNTEER_COLLECTION, RESOURCE_COLLECTION
from feeder.common.utils import save_data_json
from feeder.resource_transformer import process_suply_feed
from feeder.volunteer_transformer import process_volunteer_feed


def get_id(camp_name):
    log("Processing camp " + str(camp_name))
    return slugify(camp_name)


def get_solr_feed_file(json_file, must_fields=None):
    with open(json_file) as fh:
        data_frame = pd.read_json(fh, dtype=False)
        if isinstance(must_fields, list) and len(must_fields) != 0:
            data_frame.dropna(subset=must_fields, inplace=True)
        return data_frame


def process(sheet_url, collection):
    json_file = save_data_json(sheet_url, True)
    data_frame = get_solr_feed_file(json_file, must_fields=['campName'])
    csv_file = json_file.replace(".json", ".csv")
    if collection == CAMP_COLLECTION:
        process_camps_feed(data_frame, csv_file)
    elif collection == VOLUNTEER_COLLECTION:
        process_volunteer_feed(data_frame, csv_file)
    else:
        process_suply_feed(data_frame, csv_file)
    feed_csv_to_solr(collection, csv_file)


# MAIN
process(CAMP_SHEET, CAMP_COLLECTION)
process(VOLUNTEER_SHEET, VOLUNTEER_COLLECTION)
process(RESOURCE_SHEET, RESOURCE_COLLECTION)
