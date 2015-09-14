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



    def get_models(self):
        retval = {}
        makeCount = 0
        modelCount = 0
        modelList = []

        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/makes', params=payload)
        json_object = json.loads(r.text)

        for make in json_object['makes']:
            for model in json_object['makes'][makeCount]['models']:
                modelList.append(json_object['makes'][makeCount]['models'][modelCount]['name'])
                modelCount += 1
            retval[make['name']] = modelList
            makeCount += 1
            modelCount = 0
            modelList = []

        return retval

    def get_years(self):
        retval = {}
        makeCount = 0
        modelCount = 0
        yearCount = 0
        modelList = []
        yearList = []

        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/makes', params=payload)
        json_object = json.loads(r.text)
"""
        for make in json_object['makes']:
            for model in json_object['makes'][makeCount]['models']:
                for year in json_object['makes'][makeCount]['models'][modelCount]['years']:
                    yearList.append(json_object['makes'][makeCount]['models'][modelCount]['years'][yearCount]['year'])
                    yearCount += 1
                modelList.append(json_object['makes'][makeCount]['models'][modelCount]['name'])
                modelList.append(yearList)
                modelCount += 1
                yearCount = 0
                yearList = []
            retval[make['name']] = modelList
            makeCount += 1
            modelCount = 0

        return retval
"""