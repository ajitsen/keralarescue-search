# This document declares various indexes created in elastic

# Add new fields
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-put-mapping.html
CAMP_INDEX_DEF = {
  "mappings": {
    "_doc": {
      "properties": {
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

