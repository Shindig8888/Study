import requests
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
WEIGHT = "75"
HEIGHT = "173"
AGE = 29

workout_input = input("Tell me which excercises you did: ")

workout_config = {
    "query": workout_input,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE

}

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
  }

request = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise', json=workout_config, headers=headers)
request.raise_for_status()
print(dict(request.json()))

workout_data = request.json()

excercise_type = []
duration = []
calories = []

for workout in workout_data['exercises']:
    excercise_type.append(workout['name'])
    duration.append(workout['duration_min'])
    calories.append(workout['nf_calories'])

TOKEN = os.getenv("TOKEN", "No valid token found")
headers = {
    "Authorization": f"Bearer {TOKEN}"
}

sheet_endpoint = "	https://sheetdb.io/api/v1/0y7q4l6aipbf7"
for n in range(0, len(excercise_type)):
    now = dt.now().strftime("%d/%m/%Y")
    time = dt.now().strftime("%H:%M:%S")
    sheet_config = {
        "Date": now,
        "Time": time,
        "Exercise": excercise_type[n].title(),
        "Duration": duration[n],
        "Calories": calories[n]
    }
    request = requests.post(url=sheet_endpoint, json=sheet_config, headers=headers)
    print(request.text)

