import common.config as config
from elastic.elastic_helper import get_elastic_client, create_index
from elastic.elastic_index_def import KERALA_RESCUE_INDEX_DEF, DEMAND_INDEX_DEF



# Running again will throw 400 - index already exists exception

client = get_elastic_client()
results = create_index(client, index=config.ELASTIC_INDEX, mapping_settings=KERALA_RESCUE_INDEX_DEF)
print(results)


