from feeder.camp_transformer import process_camps_feed
from feeder.common.config import CAMP_SHEET, RESOURCE_SHEET, VOLUNTEER_SHEET
from feeder.common.solr_helper import CAMP_COLLECTION, feed_csv_to_solr, VOLUNTEER_COLLECTION, RESOURCE_COLLECTION, \
    get_data_frame_from_json
from feeder.common.utils import save_data_json
from feeder.resource_transformer import process_supply_feed
from feeder.volunteer_transformer import process_volunteer_feed


def process(sheet_url, collection):
    json_file = save_data_json(sheet_url)
    csv_file = json_file.replace(".json", ".csv")

    if collection == CAMP_COLLECTION:
        data_frame = get_data_frame_from_json(json_file, must_fields=['campName'])
        process_camps_feed(data_frame, csv_file)
    elif collection == VOLUNTEER_COLLECTION:
        data_frame = get_data_frame_from_json(json_file, must_fields=['mobileNumber'])
        process_volunteer_feed(data_frame, csv_file)
    else:
        data_frame = get_data_frame_from_json(json_file, must_fields=['contactDetails'])
        process_supply_feed(data_frame, csv_file)
    feed_csv_to_solr(collection, csv_file)


# MAIN
process(CAMP_SHEET, CAMP_COLLECTION)
process(VOLUNTEER_SHEET, VOLUNTEER_COLLECTION)
process(RESOURCE_SHEET, RESOURCE_COLLECTION)
