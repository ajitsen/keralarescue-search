import pandas as pd


import common.data as data
from common.logger import log


def process_camp_feed(data_frame, csv_file, elastic_bulk_file):
    data_frame['campName'] = pd.Series([data.get_clean_str(camp_name) for camp_name in data_frame['campName']])
    data_frame['id'] = pd.Series([data.get_camp_id(camp_name, phone) for camp_name, phone in zip(data_frame['campName'], data_frame['contactNo'])])
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


    log("========= Data size ======")
    log(data_frame.shape)
    log(data_frame.dtypes)
    log("==========================")

    create_solr_feed(csv_file, data_frame.copy())
    create_elastic_feed(elastic_bulk_file, data_frame.copy())


def create_solr_feed(csv_file, data_frame_copy):
    data_frame_copy.rename(columns={
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
    data_frame_copy.to_csv(csv_file, encoding="utf-8", index=False)


def create_elastic_feed(elastic_bulk_file, data_frame_copy):
    # FIXME derive status - open closed
    data_frame_copy['status'] = pd.Series(["open" for code in data_frame_copy['campName']])

    data_frame_copy.rename(columns={
        'campName': 'camp_name',
        'pointOfContact': 'contact_name',
        'contactNo': 'contact_phone',
        'needs': 'demand',
        'excess': 'excess',
        'timeOfUpdate': 'time_updated_str',
        'strength': 'people_count_str',
        'location': 'place',

        'id': 'id',
        'district_full': 'district',
        'last_modified': 'time_updated',
        'latlng': 'latlng',
        'total_strength': 'people_count',
        'status': 'status'
    }, inplace=True)
    # pd.set_option('display.max_rows', -1)
    # pd.set_option('display.max_columns', None)
    # pd.set_option('display.expand_frame_repr', False)
    # pd.set_option('max_colwidth', -1)
    # print(data_frame_copy[['id', 'camp_name', 'contact_phone']])
    data_frame_copy.to_csv(elastic_bulk_file, encoding="utf-8", index=False)

