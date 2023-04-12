import requests
from datetime import datetime
GENDER = "male"
WEIGHT_KG = 79.2
HEIGHT_CM = 176.2
AGE = 26


APP_ID = "af9c1d4b"
API_KEY = "7c9406ed5a54bee259cee34ff0ab4459"
TOKEN = "Bearer xcesion12578963"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/cac6f90a8cf094b404c10a64c41348af/exercise/sheet1"
exercise_input = input("How long did you exercise? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
 "query" : exercise_input,
 "gender": GENDER,
 "weight_kg": WEIGHT_KG,
 "height_cm": HEIGHT_CM,
 "age": AGE,
}

response = requests.post(url = exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": TOKEN
}

for exercise in result["exercises"]:
    exercise_input = {
        "sheet1" : {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(sheet_endpoint, json=exercise_input, headers=bearer_headers)
print(sheet_response.text)
