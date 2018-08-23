import math
import re

from slugify import slugify

from common.logger import log


def get_dist_name(dist_search_str):
    if not dist_search_str:
        return

    code_to_name = {
              'tvm': 'Thiruvananthapuram',
              'ptm': 'Pathanamthitta',
              'alp': 'Alappuzha',
              'ktm': 'Kottayam',
              'idk': 'Idukki',
              'mpm': 'Malappuram',
              'koz': 'Kozhikode',
              'wnd': 'Wayanad',
              'knr': 'Kannur',
              'ksr': 'Kasaragod',
              'pkd': 'Palakkad',
              'tcr': 'Thrissur',
              'ekm': 'Ernakulam',
              'kol': 'Kollam'
    }
    if dist_search_str in code_to_name:
        return code_to_name[dist_search_str]

    dist_search_str = dist_search_str.strip().lower()
    for name in code_to_name.values():
        if name.lower() in dist_search_str:
            return name


def get_location_concact(location):
    (camp, addr, region) = location
    string = ''
    if camp:
        string += str(camp).strip()

    if addr and addr != '' and isinstance(addr, str):
        for part in addr.split(','):
            part = part.strip()
            if part.lower() not in string.lower() and part != '':
                if string != '':
                    string += ', '
                string += part

    if region and region != '' and isinstance(region, str):
        if string != '':
            string += ', '
        string += str(region).strip()

    return string


def get_camp_id(camp_name, phone):
    camp_id = ''
    if camp_name and isinstance(camp_name, str) and camp_name != '':
        camp_name = str(camp_name)
        if '-' in camp_name:
            camp_name = camp_name.split('-')[0]
        camp_id = slugify(camp_name)
    if len(camp_id) < 2 and phone:
        phone = get_clean_str(phone)
        camp_id = slugify(phone)
    log("Camp id: " + camp_id)
    return camp_id


def get_clean_str(string):
    string = str(string)
    if not string or not isinstance(string, str):
        return ''
    string = string.translate(' \n\t\r')
    return ' '.join(string.split())


def get_clean_json_data(title):
    if isinstance(title, str):
        for ch in "'\"*=/&^#@":
            title = title.replace(ch, '')
    return get_clean_str(title)


def get_person_gender(gender_0_m):
    if gender_0_m and ((isinstance(gender_0_m, float) and not math.isnan(gender_0_m)) or isinstance(gender_0_m, int)):
        if gender_0_m > 0.5:
            return "male"
        else:
            return "female"
    else:
        return "not-set"


def get_person_time(date_str):
    # 2018-08-18 17:26:54.283864+00:00 to 2018-08-18T17:26:54Z
    if date_str and isinstance(date_str, str) and len(date_str) > 20:
        date, rest = date_str.split(' ')
        time = ''
        if rest:
            time = rest.split('.')[0]
        return date + "T" + time + "Z"
    # Default Value
    return '2018-08-15T00:00:00Z'


def get_clean_int(param):
    if isinstance(param, int):
        return param
    if isinstance(param, str):
        matched = re.search(r'\d+', param)
        if matched:
            return int(matched.group())
    return 0
