import pandas as pd

import common.config as config
import common.data as data
from common.logger import log



def process_camp_feed(data_frame, csv_file):
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
    return create_elastic_feed(data_frame.copy(), config.ELASTIC_INDEX, config.ELASTIC_CAMP_TYPE)


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


def create_elastic_feed(data_frame_copy, elastic_index, data_type):

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

    elastic_fields = [
        'id',
        'camp_name',
        'contact_name',
        'contact_phone',
        'demand',
        'excess',
        'time_updated_str',
        'people_count_str',
        'place',
        'district',
        'time_updated',
        'latlng',
        'people_count',
        'status'
    ]

    bulk_actions = []
    for i, row in data_frame_copy.filter(items=elastic_fields).iterrows():
        data_id = data.get_clean_json_data(row['id'])
        if data_id == '':
            continue

        action = {
            "_index": elastic_index,
            "_type": "_doc",
            "_id":  data_id,
            "_source": {
                'data_type': data_type,
                'id': data_type+'-'+data_id,
                'camp_name': data.get_clean_json_data(row['camp_name']),
                'contact_name': data.get_clean_json_data(row['contact_name']),
                'contact_phone': data.get_clean_json_data(row['contact_phone']),
                'demand': data.get_clean_json_data(row['demand']),
                'excess': data.get_clean_json_data(row['excess']),
                'time_updated_str': data.get_clean_json_data(row['time_updated_str']),
                'people_count_str': data.get_clean_json_data(row['people_count_str']),
                'place': data.get_clean_json_data(row['place']),
                'district': data.get_clean_json_data(row['district']),
                'time_updated': data.get_clean_json_data(row['time_updated']),
                'latlng': row['latlng'],
                'people_count': row['people_count'],
                'status': data.get_clean_json_data(row['status'])
            }
        }
        bulk_actions.append(action)
    return bulk_actions

