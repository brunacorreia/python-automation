# source: https://www.upcitemdb.com/api/explorer#!/lookup/get_trial_lookup
from urllib import response
import requests
import json

# request to an api
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '0012993441012'}
response = requests.get(baseUrl, params = parameters)
print(response.url)

# parsing through JSON
content = response.content
info = json.loads(content) # loads -> function that converts json docs into dictionaries
print(type(info)) # <class 'dict'> OK

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)