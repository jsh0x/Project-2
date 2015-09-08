__author__ = 'jsh0x'
import requests
import json

matchSuccess = 0
makeCount = 0
modelCount = 0
yearCount = 0
Makes = ''
Models = ''
Years = ''

r = requests.get('https://api.edmunds.com/api/vehicle/v2/makes?fmt=json&api_key=rpftuam8pj4dawg5nauq8vs5')
json_object = json.loads(r.text)

#Creates a list of makes
for makes in json_object['makes']:
    Makes = Makes + str(json_object['makes'][makeCount]['name']) + "\n"
    makeCount += 1
makeCount = 0

Make = raw_input("Car Make?\n" + Makes)

#Checks that the make is correct
for makes in json_object['makes']:
    if Make == json_object['makes'][makeCount]['name']:
        matchSuccess = 1
        break
    elif Make != json_object['makes'][makeCount]['name'] and makeCount == makes:
        matchSuccess = 0
        print "unknown make"
        break
    else:
        makeCount += 1

#Creates a list of models for the selected make
for models in json_object['makes'][makeCount]['models']:
    Models = Models + str(json_object['makes'][makeCount]['models'][modelCount]['name']) + "\n"
    modelCount += 1
modelCount = 0

if matchSuccess == 1:
    Model = raw_input("Car Model?\n" + Models)

#Checks that the model is correct
    for models in json_object['makes'][makeCount]['models']:
        if Model == json_object['makes'][makeCount]['models'][modelCount]['name']:
            matchSuccess = 1
            break
        elif Model != json_object['makes'][makeCount]['models'][modelCount]['name'] and modelCount == models:
            matchSuccess = 0
            print "unknown model"
            break
        else:
            modelCount += 1

#Creates a list of years for the selected model
for years in json_object['makes'][makeCount]['models'][modelCount]['years']:
    Years = Years + str(json_object['makes'][makeCount]['models'][modelCount]['years'][yearCount]['year']) + "\n"
    yearCount += 1
yearCount = 0

if matchSuccess == 1:
    Year = raw_input("Car Model Year?\n" + Years)

#Checks that year is correct
    for years in json_object['makes'][makeCount]['models'][modelCount]['years']:
        if Year == json_object['makes'][makeCount]['models'][modelCount]['years'][yearCount]['year']:
            matchSuccess = 1
            break
        elif Year != json_object['makes'][makeCount]['models'][modelCount]['years'][yearCount]['year'] and yearCount == years:
            matchSuccess = 0
            print "unknown year"
            break
        else:
            yearCount += 1

if matchSuccess == 1:
    print Year + ' ' + Make + ' ' + Model


#Style = raw_input("Car Style?")
