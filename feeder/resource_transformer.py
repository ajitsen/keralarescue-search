import pandas as pd

from common.logger import log

def match_str(value, expected):
    return value and isinstance(value, str) and value.lower() == expected.lower()


def process_supply_feed(data_frame, csv_file):
    data_frame['id'] = pd.Series([num for num in data_frame['contactDetails']])

    # TODO add district
    data_frame['district_full'] = pd.Series(["District" for code in data_frame["location(rough)"]])
    # TODO add organization
    data_frame['organisations'] = pd.Series(["Organization" for code in data_frame["contactDetails"]])
    data_frame['verified'] = pd.Series([match_str(val, 'verified') for val in data_frame['verifiedOrNot']])
    data_frame['available'] = pd.Series([match_str(val, 'available') for val in data_frame['availability']])

    data_frame.drop(columns=['availability', 'verifiedOrNot'], inplace=True)

    log("========= Data size ======")
    log(data_frame.shape)
    log(data_frame.dtypes)
    data_frame.rename(columns={
        'nameOfPeople': 'name_t',
        'contactDetails': 'contact_no_t',
        'recourcesAvailableWithThem': 'offer_t',
        'location(rough)': 'place_s',
        'comments': 'comments_t',
        'verifiedBy': 'verified_by_s',

        'id': 'id',
        'verified': 'verified_b',
        'available': 'available_b',
        'district_full': 'district_full_t',
        'organisations': 'organisations'
    }, inplace=True)
    data_frame.to_csv(csv_file, encoding="utf-8", index=False)
    return csv_file
