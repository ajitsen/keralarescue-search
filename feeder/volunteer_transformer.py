import pandas as pd

from common.logger import log


def has_car(car):
    return car and isinstance(car, str) and car.lower() in ["car", "yes"]


def has_bike(bike):
    return bike and isinstance(bike, str) and bike.lower() in ["bike", "yes"]


def get_vehicle(car_bike):
    (car, bike) = car_bike
    string = ''
    if has_car(car):
        string += "car "
    if has_bike(bike):
        string += "bike"
    return string


def process_volunteer_feed(data_frame, csv_file):

    data_frame['id'] = pd.Series([num for num in data_frame['mobileNumber']])
    data_frame['vehicle'] = pd.Series([get_vehicle(car_bike) for car_bike in zip(data_frame['car'], data_frame['bike'])])
    data_frame['car_b'] = pd.Series([has_car(car) for car in data_frame['car']])
    data_frame['bike_b'] = pd.Series([has_bike(bike) for bike in data_frame['bike']])
    # FIXME add district
    data_frame['district_full'] = pd.Series(["District" for code in data_frame['location']])

    data_frame.drop(columns=['car', 'bike'], inplace=True)

    log("========= Data size ======")
    log(data_frame.shape)
    log(data_frame.dtypes)
    data_frame.rename(columns={
        'name': 'name_t',
        'mobileNumber': 'contact_no_t',
        'canArrange/Offer': 'offer_t',
        'location': 'place_s',
        'organisations': 'organisations',
        'comments': 'comments_t',

        'id': 'id',
        'car_b': 'car_b',
        'bike_b': 'bike_b',
        'vehicle': 'vehicle_t',
        'district_full': 'district_full_t'
    }, inplace=True)
    data_frame.to_csv(csv_file, encoding="utf-8", index=False)
    return csv_file


