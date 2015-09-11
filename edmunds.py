import requests
import json

class Edmunds:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_makes(self):
        # returns a dictionary of makes|id
        retval = {}

        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/makes', params=payload)
        json_object = json.loads(r.text)

        for make in json_object['makes']:
            retval[make['name']] = make['id']

        return retval

