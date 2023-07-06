import requests
from datetime import datetime

MY_LAT = 53.904541
MY_LNG = 27.561523

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunset)
print(sunset.split("T"))

time_now = datetime.now()
print(time_now.hour)
