from common.config import ELASTIC_CAMP_INDEX
from common.elastic_helper import get_elastic_client, create_index
from common.elastic_index_def import CAMP_INDEX_DEF


def create_index_camp():
    client = get_elastic_client()
    results = create_index(client=client, index=ELASTIC_CAMP_INDEX, mapping_settings=CAMP_INDEX_DEF)
    print(results)

# Running again will throw 400 - index already exists exception
# create_index_camp()

