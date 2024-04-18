import requests
from datetime import datetime
import time
import smtplib


MY_LAT = 37.51684337188134 # Your latitude
MY_LONG = 127.03936120321963 # Your longitude

parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid":'Asia/Seoul'
    }

        
def is_iss_above():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(iss_latitude)
    print(round(MY_LAT,2))
    print(iss_longitude)
    print(round(MY_LONG,2))

    return ((MY_LAT+5) >=iss_latitude >= (MY_LAT-5)) and ((MY_LONG+5) >= iss_longitude >= (MY_LONG-5))

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour_now = time_now.hour

    print(hour_now)

    return hour_now < sunrise or hour_now > sunset

def send_email():
    #send email
    my_email = "calixatexample@gmail.com"
    password = 'stgs szlt fpmm onss'
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password )
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg="Subject:ISS is above your head!\n\nISS is above your head!"
            )


while True:
    if is_iss_above() and is_dark():
        send_email()

    print(is_dark())

    time.sleep(60)



