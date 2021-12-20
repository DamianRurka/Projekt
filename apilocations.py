import requests
import json
# set up the request parameters
params = {
  'api_key': '80504B43034D40A1A3C90E691512907E',
  'search_type': 'place_details',
  'data_id': '0x89c259cea3b62d4d:0x4519bf551f37923f',
  'output': 'json',
  'hl': 'pl'
}

# make the http GET request to Scale SERP
api_result = requests.get('https://api.scaleserp.com/search', params)

# print the JSON response from Scale SERP
print(json.dumps(api_result.json()))
