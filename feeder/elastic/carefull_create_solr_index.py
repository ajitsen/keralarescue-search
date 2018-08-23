from common.config import ELASTIC_CAMP_INDEX, ELASTIC_DEMAND_INDEX
from common.elastic_helper import get_elastic_client, create_index
from elastic.elastic_index_def import CAMP_INDEX_DEF, DEMAND_INDEX_DEF


def create_index_camp():
    results = create_index(client, index=ELASTIC_CAMP_INDEX, mapping_settings=CAMP_INDEX_DEF)
    print(results)


def create_demand_camp():
    results = create_index(client, index=ELASTIC_DEMAND_INDEX, mapping_settings=DEMAND_INDEX_DEF)
    print(results)

# Running again will throw 400 - index already exists exception

client = get_elastic_client()

# create_index_camp()

# create_demand_camp()

