#!/home/ajitsen/PythonEnvironments/kr_search/bin/python

from camp_transformer import process_camp_feed
from common.config import CAMP_SHEET, VOLUNTEER_SHEET, RESOURCE_SHEET
from common.solr_helper import CAMP_COLLECTION, get_data_frame_from_json, feed_csv_to_solr, VOLUNTEER_COLLECTION, \
    RESOURCE_COLLECTION
from common.utils import save_data_json
from elastic.elastic_helper import feed_bulk_to_elastic
from resource_transformer import process_supply_feed
from volunteer_transformer import process_volunteer_feed


def process(sheet_url, solr_collection):
    # Fixme - remove cache param in production
    json_file = save_data_json(sheet_url, cache=True)
    csv_file = json_file.replace(".json", ".csv")
    elastic_bulk_actions = []
    if sheet_url == CAMP_SHEET:
        data_frame = get_data_frame_from_json(json_file)
        elastic_bulk_actions = process_camp_feed(data_frame, csv_file)

    elif sheet_url == VOLUNTEER_SHEET:
        data_frame = get_data_frame_from_json(json_file, must_fields=['mobileNumber'])
        process_volunteer_feed(data_frame, csv_file)

    else:
        data_frame = get_data_frame_from_json(json_file, must_fields=['contactDetails'])
        process_supply_feed(data_frame, csv_file)

    feed_csv_to_solr(solr_collection, csv_file)
    feed_bulk_to_elastic(elastic_bulk_actions)


# MAIN
process(CAMP_SHEET, CAMP_COLLECTION)
process(VOLUNTEER_SHEET, VOLUNTEER_COLLECTION)
process(RESOURCE_SHEET, RESOURCE_COLLECTION)
