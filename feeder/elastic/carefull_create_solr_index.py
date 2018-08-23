import common.config as config
from elastic.elastic_helper import get_elastic_client, create_index
import elastic.elastic_index_def as index_def



# Running again will throw 400 - index already exists exception
client = get_elastic_client()
results = create_index(client, index=config.ELASTIC_PERSON_INDEX, mapping_settings=index_def.PERSON_INDEX_DEF)
print(results)


