import requests
from datetime import datetime as dt
import json
from twilio.rest import Client

account_sid = 
auth_token = 

LAT = 37.50494289803385
LONG = 126.94782832030906

api = "https://api.open-meteo.com/v1/forecast?latitude=37.50494289803385&longitude=126.94782832030906&hourly=temperature_2m,weather_code&timezone=Asia%2FTokyo&forecast_days=2"

def rain_string(rain_hour, rain_value):
    rain_string = ""
    if len(rain_hour)!=0:
        for n in range(0, len(rain_hour)):
            if n==0:
                rain_string += f"오늘은 {rain_hour[n]}시부터 {rain_value[n]}시간동안, \n"
            elif n==len(rain_hour)-1:
                rain_string += f"{rain_hour[n]}시부터 {rain_value[n]} 시간동안 \n"
            else:
                rain_string += f"{rain_hour[n]}시부터 {rain_value[n]} 시간동안, \n"
        rain_string += "비 혹은 눈이 내리겠습니다. 우산챙기세요!"
    else:
        rain_string += "오늘은 지금으로부터 12시간동안 화창합니다!"
    return rain_string

year_now = dt.now().year
month_now = dt.now().month
day_now = dt.now().day
hour_now = dt.now().hour
minute_now = dt.now().minute

request = requests.get(api)
request.raise_for_status()
weather_data = request.json()

weather_time = weather_data["hourly"]["time"]
weather_hour = [timestring.split("T")[1].split(":")[0] for timestring in weather_time]

weather_code = weather_data["hourly"]['weather_code']
weather_temperature = weather_data["hourly"]['temperature_2m']

weathercode_rain = [i for i in range(51, 100)]

rain_list = []
for n in range(hour_now, hour_now+12):
    if int(weather_code[n]) in  weathercode_rain:
        rain_list.append(True)
    else:
        rain_list.append(False)

rain_count = 0
rain_count_hour = []
rain_count_values = []
for n in range(0, len(rain_list)):
    if n==0 and rain_list[n]:
        rain_count_hour.append(hour_now+n)
        rain_count+=1
    elif n==0 and not rain_list:
        pass
    elif n == len(rain_list)-1 and rain_list[n-1] and rain_list[n]:
        rain_count+=1
        rain_count_values.append(rain_count)
    elif rain_list[n] and not rain_list[n-1]:
        rain_count_hour.append(hour_now+n)
        rain_count+=1
    elif rain_list[n] and rain_list[n-1]:
        rain_count+=1
    elif not rain_list[n] and rain_list[-1]:
        rain_count_values.append(rain_count)
        rain_count = 0

rainday_string = rain_string(rain_count_hour, rain_count_values)

client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f"{rainday_string}",
    from_="+12513330579",
    to="+821033393818"
)

print(message.status)


    

# python 콘솔에서:
# export TWILIO_TOKEN=464411313bc035473019e8b5996b13a3
# export TWILIO_SID=AC565f15f515bb34c6240ff6815d0a8f2d
# export PHONE_FROM=+12513330579
# export PHONE_TO=+821033393818

# import os
# os.inviron.get("TWILIO_TOKEN")