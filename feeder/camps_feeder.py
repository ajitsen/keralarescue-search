#!/home/ajitsen/PythonEnvironments/kr_search/bin/python

from camp_transformer import process_camp_feed
from common.config import CAMP_SHEET, RESOURCE_SHEET, VOLUNTEER_SHEET
from common.solr_helper import CAMP_COLLECTION, feed_csv_to_solr, VOLUNTEER_COLLECTION, RESOURCE_COLLECTION, \
    get_data_frame_from_json
from common.utils import save_data_json
from resource_transformer import process_supply_feed
from volunteer_transformer import process_volunteer_feed


def process(sheet_url, collection):
    # Fixme - remove cache param in production
    json_file = save_data_json(sheet_url, cache=True)
    csv_file = json_file.replace(".json", ".csv")
    elastic_bulk_feed_file = json_file.replace(".json", ".elastic_feed")
    if collection == CAMP_COLLECTION:
        data_frame = get_data_frame_from_json(json_file)
        process_camp_feed(data_frame, csv_file, elastic_bulk_feed_file)

    elif collection == VOLUNTEER_COLLECTION:
        data_frame = get_data_frame_from_json(json_file, must_fields=['mobileNumber'])
        process_volunteer_feed(data_frame, csv_file)
    else:
        data_frame = get_data_frame_from_json(json_file, must_fields=['contactDetails'])
        process_supply_feed(data_frame, csv_file)

    # Fixme uncomment
    #feed_csv_to_solr(collection, csv_file)


# MAIN
process(CAMP_SHEET, CAMP_COLLECTION)
#process(VOLUNTEER_SHEET, VOLUNTEER_COLLECTION)
#process(RESOURCE_SHEET, RESOURCE_COLLECTION)
