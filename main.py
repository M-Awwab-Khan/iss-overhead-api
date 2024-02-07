import requests
import datetime as dt

params = {
    'lat': 24.860735,
    'lng': 67.001137,
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()

sunrise = response.json()['results']['sunrise'].split('T')[-1].split(':')[0]
sunset = response.json()['results']['sunset'].split('T')[-1].split(':')[0]

print(sunrise)
print(sunset)