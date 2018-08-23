import math

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
    log("Processing camp: [" + str(camp_name) +"] [" + str(phone))

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
        for ch in "'\"*=/,&^#@":
            title = title.replace(ch, '')
    return get_clean_str(title)
