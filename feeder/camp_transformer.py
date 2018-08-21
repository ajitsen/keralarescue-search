import pandas as pd
from slugify import slugify

from common.logger import log


def process_camps_feed(data_frame, csv_file):
    data_frame['id'] = pd.Series([get_camp_id(camp_name) for camp_name in data_frame['campName']])
    # FIXME add logic to call place finder
    data_frame['latlng'] = pd.Series(['29.327685626916956,48.055961771640426' for location in data_frame['campName']])
    # FIXME add district
    data_frame['district_full'] = pd.Series(["District" for code in data_frame['campName']])
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


def get_camp_id(camp_name):
    log("Processing camp " + str(camp_name))
    return slugify(camp_name)
