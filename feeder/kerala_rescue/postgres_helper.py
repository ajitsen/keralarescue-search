import numpy as np
import pandas as pd
import psycopg2

import cred
from common.logger import log


def get_db_connection():
    try:
        # use our connection values to establish a connection
        return psycopg2.connect(cred.KERALA_RESCUE_DB)
    except Exception as e:
        log("Error connecting to kerala_rescue db::::", error=True)
        log(e)
    return None



def get_person_details_as_data_frame(conn, last_person_id, offset, limit):
    try:
        sql_query = """
SELECT p.id, p.name, p.phone, p.age, p.gender, p.address, p.district, p.notes, p.added_at, p.checkin_date,
p.checkout_date, p.status, c.id as camp_id, c.name as camp_name, c.location as camp_location,
c.district as camp_district, c.latlng as latlng
FROM mainapp_person AS p
LEFT JOIN mainapp_rescuecamp AS c
ON p.id > """ + str(last_person_id) + """ AND p.camped_at_id = c.id
ORDER BY p.id ASC OFFSET """ + str(offset) + " LIMIT  " + str(limit)
        data_frame = pd.read_sql(sql_query, conn)
        return data_frame.replace(np.nan, ' ', regex=True)
    except Exception as e:
        print("Error getting data ")
        print(e)


