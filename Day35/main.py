import requests
import smtplib
import os


LAT = 4.05
LON = 9.69
api_key = "KEY"


MY_EMAIL = "aminaousmanu@gmail.com"
PASSWORD = "PASSWORD"

parameters = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

data = response.json()

hourly_data = [data["list"][:12]]

condition_code_list = [hourly_data[0][item]["weather"][0]["id"] for item in range(len(hourly_data[0]))]

rain_fall = False

for code in condition_code_list:
    if code > 700:
        rain_fall = True

if rain_fall:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="borispokwangeh@gmail.com",
            msg="Subject:Take an umbrella\n\nIt will definitely rain today. So dress up for it and watch out"
        )