# This document declares various indexes created in elastic

# Add new fields
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-put-mapping.html
KERALA_RESCUE_INDEX_DEF = {
  "mappings": {
    "_doc": {
      "properties": {
        "data_type": {
          "type": "keyword"
        },
        "camp_name": {
          "type": "text"
        },
        "contact_name": {
          "type": "text"
        },
        "contact_phone": {
          "type": "text"
        },
        "demand": {
          "type": "text",
          "fields": {
            "keyword": {
              "type":  "keyword",
              "ignore_above": 100
            }
          }
        },
        "excess": {
          "type": "text"
        },
        "time_updated_str": {
          "type": "text"
        },
        "people_count_str": {
          "type": "text",
          "index": "false"
        },
        "place": {
          "type": "text"
        },
        "id": {
          "type": "keyword"
        },
        "district": {
          "type": "keyword"
        },
        "time_updated": {
          "type": "date"
        },
        "latlng": {
          "type": "geo_point"
        },
        "status": {
          "type": "keyword"
        },
        "people_count": {
          "type": "short"
        }
      }
    }
  },
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 1
    }
  }
}


# Person Index definition - Searching persons at Camps
# It needs a separate index since it has about 1.5L people
# and this could demand more search volume

PERSON_INDEX_DEF = {
  "mappings": {
    "_doc": {
      "properties": {
        "id": {
          "type": "integer"
        },
        "name": {
          "type": "text"
        },
        "phone": {
          "type": "text"
        },
        "age": {
          "type": "short"
        },
        "gender": {
          "type": "keyword"
        },
        "address": {
          "type": "text"
        },
        "district": {
          "type": "keyword"
        },
        "notes": {
          "type": "text"
        },
        "time_updated": {
          "type": "date"
        },
        "checkin_date": {
          "type": "date"
        },
        "checkout_date": {
          "type": "date"
        },
        "status": {
          "type": "keyword"
        },
        "camp_id": {
          "type": "integer"
        },
        "camp_name": {
          "type": "text"
        },
        "camp_location": {
          "type": "text"
        },
        "camp_district": {
          "type": "keyword"
        },
        "latlng": {
          "type": "geo_point"
        }
      }
    }
  },
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 1
    }
  }
}


# Single Demand Index,  created for every demand - Every point of time
DEMAND_INDEX_DEF = {
  "mappings": {
    "camp": {
      "properties": {
        "demand_item": {
          "type": "text"
        },
        "id": {
          "type": "keyword"
        },
        "has_met": {
          "type": "boolean"
        },
        "source_index": {
          "type": "keyword"
        },
        "source_index_id": {
          "type": "keyword"
        },
        "contact_name": {
          "type": "text"
        },
        "contact_phone": {
          "type": "text"
        },
        "time_updated_str": {
          "type": "text"
        },
        "place": {
          "type": "text"
        },
        "district": {
          "type": "keyword"
        },
        "time_updated": {
          "type": "date"
        },
        "latlng": {
          "type": "geo_point"
        },

        "people_count": {
          "type": "short"
        }
      }
    }
  },
  "settings": {
    "index": {
      "number_of_shards": 2,
      "number_of_replicas": 1
    }
  }
}

