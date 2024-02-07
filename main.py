import requests
import datetime as dt
import smtplib

MY_EMAIL = '<enter your email>'
MY_PASSWORD = '<enter your password>'
LAT = 24.860735
LNG = 67.001137
params = {
    'lat': LAT,
    'lng': LNG,
    'formatted': 0
}
response = requests.get('https://api.sunrise-sunset.org/json', params=params)
response.raise_for_status()

sunrise = int(response.json()['results']['sunrise'].split('T')[-1].split(':')[0])
sunset = int(response.json()['results']['sunset'].split('T')[-1].split(':')[0])

response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status()

longitude = float(response.json()['iss_position']['longitude'])
latitude = float(response.json()['iss_position']['latitude'])

def is_close(iss_lat, iss_lng):
    if abs(abs(LAT) - abs(iss_lat)) <=5 and abs(abs(LNG) - abs(iss_lng)):
        return True
    return False

def is_dark():
    hour = dt.datetime.now().hour()
    return (24 > hour >= 20 ) and (0 <= hour <= 5)

if is_close(latitude, longitude) and is_dark():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg='Subject:Watch out for ISS Satellite\n\nISS Satellite is overhead and it is a good time to see it.'
        )