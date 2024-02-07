import requests

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

print((latitude, longitude))