import json

import numpy as np

import common.config as config
from common import data
from common.logger import log
from elastic.elastic_helper import feed_bulk_to_elastic
from kerala_rescue.postgres_helper import get_db_connection, get_person_details_as_data_frame


def save_json_to_file(file_name, bulk_actions):
    with open(file_name, "w") as fh:
        fh.write(json.dumps(bulk_actions))
        fh.close()


def fetch_data_and_process():
    conn = get_db_connection()
    limit = 300
    last_person_id = 0
    for offset in range(0, 10000, limit):
        log("Getting from from:" + str(offset) + " to:" + str(offset + limit) + " last_person:" + str(last_person_id))
        df = get_person_details_as_data_frame(conn, last_person_id, offset, limit)
        df.replace(np.nan, ' ', regex=True)
        print(df[['name', 'gender']])
        last_person_id = df['id'].tail(1).values.tolist()[-1]
        bulk_actions = create_person_elastic_feed(df.copy(), config.ELASTIC_PERSON_INDEX)
        save_json_to_file('/tmp/bulk_feed-' + str(last_person_id), bulk_actions)
        result = feed_bulk_to_elastic(bulk_actions)
        save_json_to_file('/tmp/bulk_result-' + str(last_person_id), result)


def create_person_elastic_feed(data_frame_copy, elastic_index):
    data_frame_copy.rename(columns={
        'id': 'id',
        'name': 'name',
        'phone': 'phone',
        'age': 'age',
        'gender': 'gender',
        'address': 'address',
        'district': 'district',
        'notes': 'notes',
        'added_at': 'time_updated',
        'checkin_date': 'checkin_date',
        'checkout_date': 'checkout_date',
        'status': 'status',
        'camp_id': 'camp_id',
        'camp_name': 'camp_name',
        'camp_location': 'camp_location',
        'camp_district': 'camp_district',
        'latlng': 'latlng'
    }, inplace=True)

    elastic_fields = [
        'id',
        'name',
        'phone',
        'age',
        'gender',
        'address',
        'district',
        'notes',
        'time_updated',
        'checkin_date',
        'checkout_date',
        'status',
        'camp_id',
        'camp_name',
        'camp_location',
        'camp_district',
        'latlng'
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
                'id': data_id,
                'name': data.get_clean_json_data(row['name']),
                'phone': data.get_clean_json_data(row['phone']),
                'age': data.get_clean_int(row['age']),
                'gender': data.get_person_gender(row['gender']),
                'address': data.get_clean_json_data(row['address']),
                'district': data.get_clean_json_data(data.get_dist_name(row['district'])),
                'notes': data.get_clean_json_data(row['notes']),
                'time_updated': data.get_person_time(row['time_updated']),
                'checkin_date': data.get_person_time(row['checkin_date']),
                'checkout_date': data.get_person_time(row['checkout_date']),
                'status': data.get_clean_json_data(row['status']),
                'camp_id': data.get_clean_int(row['camp_id']),
                'camp_name': data.get_clean_json_data(row['camp_name']),
                'camp_location': data.get_clean_json_data(row['camp_location']),
                'camp_district': data.get_clean_json_data(data.get_dist_name(row['camp_district'])),
                'latlng': data.get_clean_json_data(row['latlng'])
            }
        }
        bulk_actions.append(action)
    return bulk_actions


fetch_data_and_process()
