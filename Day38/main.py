import requests
import datetime as dt

today = dt.datetime.now()

NUTRITION_KEY = "522530398c5bdc4c4fd9311fd261f96e"
NUTRITION_ID = "de99734b"

NATURAL_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENPOINT = "https://api.sheety.co/81c96d16b3847233dfc174caba89a12c/workPlan/sheet1"

natural_lan_header = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY,
}

natural_lan_param = {
    "query" : input("Which exercise did you do today? "),
    "gender":"male",
    "weight_kg":60.00,
    "height_cm":167.64,
    "age":30
}

natural_lan_response = requests.post(url=NATURAL_EXERCISE_ENDPOINT, json=natural_lan_param, headers=natural_lan_header)
natural_lan_response.raise_for_status()

data= natural_lan_response.json()

for info in (data["exercises"]):

    details = {
        "sheet1" : {
            "date" : today.strftime("%d/%m/%Y"),
            "time" : today.strftime("%H:%M:%S"),
            "exercise" : info["name"].title(),
            "duration" : info["duration_min"],
            "calories" : info["nf_calories"]
        }
    }

    post_response = requests.post(url=SHEETY_ENPOINT, json=details)
