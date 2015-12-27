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
            retval[make['name']] = make['niceName']
        return retval


    def get_models(self, make):
        retval = {}
        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/'+make+'/models', params=payload)
        json_object = json.loads(r.text)

        for model in json_object['models']:
            retval[model['name']] = model['id']
        return retval


    def get_years(self, make, model):
        retval = {}
        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/'+make+'/'+model+'/years', params=payload)
        json_object = json.loads(r.text)

        for year in json_object['years']:
            retval[year['year']] = year['id']
        return retval


    def get_styles(self, make, model, year):
        retval = {}
        payload = {'fmt': 'json', 'api_key': self.api_key}
        r = requests.get('https://api.edmunds.com/api/vehicle/v2/'+make+'/'+model+'/'+year+'/styles', params=payload)
        json_object = json.loads(r.text)

        for style in json_object['styles']:
            retval[style['name']] = style['id']
        return retval
