import requests 


API_URL = 'https://dog.ceo/api/breed/labrador/images/random/5';


params = { "count": 10 }

response = requests.get(API_URL, params=params)

status_code = response.status_code 

if status_code == 200:
  print('status code was', status_code)

else:
  print('problem with API')


response_json = response.json()

print(response_json)


