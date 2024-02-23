import requests

MY_LAT = 51.587351
MY_LON = -0.127758

parameters = {
    'lat': MY_LAT,
    'lng': MY_LON,
    'formatted': 0
}
response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()['results']
print(f"Sunrise = {data['sunrise']} and Sunset = {data['sunset']}")
