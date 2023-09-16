import requests
import datetime as dt
import math
import smtplib


LAT = 4.061536
LON = 9.786072

MY_EMAIL = "aminaousmanu@gmail.com"
PASSWORD = "PASSWORD"

current_time = dt.datetime.now()

location_response = requests.get(url="http://api.open-notify.org/iss-now.json")
location_response.raise_for_status()
location_data = location_response.json()

iss_lat = float(location_data["iss_position"]["latitude"])
iss_lon = float(location_data["iss_position"]["longitude"])

print(iss_lat)
print(iss_lon)


parameters = {
    "lat": LAT,
    "lon": LON,
    "formatted": 0
}

time_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
time_response.raise_for_status()
data = time_response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


if math.isclose(iss_lat, LAT, rel_tol=0.5) and math.isclose(iss_lon, LON, rel_tol=0.5) and (current_time.hour >= sunset or current_time.hour <= sunrise):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr= MY_EMAIL,
            to_addrs= MY_EMAIL,
            msg="Subject:LOOK UP!!!\n\nThe ISS is now upon you. Behold what wonders men can do"
        )
