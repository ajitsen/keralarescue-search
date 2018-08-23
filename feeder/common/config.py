def get_req_header():
    return {
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    }

API_URL = "https://keralarescue.in/data"
SOLR_URL = "http://localhost:8983/solr/krescue10/select"
ELASTIC_HOST = "9516548ae97247d2a26da531143fb27a.ap-southeast-1.aws.found.io"
ELASTIC_PORT = '9243'
ELASTIC_CAMP_INDEX = 'camp_index'
ELASTIC_DEMAND_INDEX = 'demand_index'

TEST_CAMP_ALAPY_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=0&single=true&output=tsv"
TEST_CAMP_PATANAM_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=504181366&single=true&output=tsv"
TEST_CAMP_ERN_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=476244282&single=true&output=tsv"
TEST_CAMP_KANNUR_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=2084744377&single=true&output=tsv"
TEST_CAMP_IDUKKI_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=1108101787&single=true&output=tsv"
TEST_CAMP_KOLLAM_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=271217651&single=true&output=tsv"
TEST_CAMP_PALAKAD_SHEET = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTkyEtVvIQtcApxe9cijuwK9QCGWVzQIdw7Fg-N2V7pCyZRFJjZ7qJ40hnQnhx-yHcYWkTSjHfJtsd3/pub?gid=960659497&single=true&output=tsv"


RESOURCE_SHEET = 'https://us-central1-relief-camp-data.cloudfunctions.net/getResourcesSheet'
CAMP_SHEET = 'https://us-central1-relief-camp-data.cloudfunctions.net/getReliefCampsSheet'
VOLUNTEER_SHEET = 'https://us-central1-relief-camp-data.cloudfunctions.net/getVolunteersSheet'
