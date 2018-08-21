import pandas as pd
from slugify import slugify

from feeder.common.config import CAMP_SHEET, RESOURCE_SHEET, VOLUNTEER_SHEET
from feeder.common.logger import log
from feeder.common.solr_helper import CAMP_COLLECTION, feed_csv_to_solr, VOLUNTEER_COLLECTION, RESOURCE_COLLECTION
from feeder.common.utils import save_data_json


def get_id(camp_name):
    log("Processing camp " + str(camp_name))
    return slugify(camp_name)


def process_camps_feed(data_frame, csv_file):
    data_frame['id'] = pd.Series([get_id(camp_name) for camp_name in data_frame['campName']])
    # FIXME add logic to call place finder
    data_frame['latlng'] = pd.Series(['29.327685626916956,48.055961771640426' for location in data_frame['campName']])
    # FIXME add district
    data_frame['district_full'] = pd.Series(["Dummy District" for code in data_frame['campName']])
    # FIXME process date modified
    data_frame['last_modified'] = pd.Series(["2018-08-16T09:19:24.604Z" for code in data_frame['campName']])
    # FIXME get processed_needs
    data_frame['need_categories'] = pd.Series(["water,sanitation" for needs in data_frame['needs']])
    # FIXME get Total Strength
    data_frame['total_strength'] = pd.Series([1000 for needs in data_frame['strength']], dtype='int64')
    data_frame['total_strength'] = data_frame.total_strength.fillna(0).astype(int)

    log("========= Json Data size ======")
    log(data_frame.shape)
    log(data_frame.dtypes)
    data_frame.rename(columns={
        'campName': 'camp_name_t',
        'pointOfContact': 'contact_t',
        'contactNo': 'contact_no_t',
        'needs': 'needs_t',
        'excess': 'excess_t',
        'timeOfUpdate': 'time_updated_t',
        'strength': 'strength_t',
        'location': 'place_s',

        'id': 'id',
        'district_full': 'district_full_s',
        'last_modified': 'last_modified',
        'latlng': 'location',
        'total_strength': 'total_strength_i',
        'need_categories': 'need_cat_ss'
    }, inplace=True)
    data_frame.to_csv(csv_file, encoding="utf-8", index=False)
    return csv_file


def get_solr_feed_file(json_file, must_fields=None):
    with open(json_file) as fh:
        data_frame = pd.read_json(fh, dtype=False)
        if isinstance(must_fields, list) and len(must_fields) != 0:
            data_frame.dropna(subset=must_fields, inplace=True)
        return data_frame


def process_volunteer_feed(data_frame, csv_file):
    pass


def process_suply_feed(data_frame, csv_file):
    pass


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
