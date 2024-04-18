#APIs
#- is a set of commands, functions, protocols, and objects
#   that programmers can use to create software or interact with an external system

#API endpoint: url, data location
import requests
import datetime as dt

# response = requests.get(url='http://api.open-notify.org/iss-now.json')

# #status code
# print(response)
# print(response.status_code)
# print(response.raise_for_status())
# #resopnse [1XX] => hold on
# #resopnse [2XX] => sucess
# #resopnse [3XX] => go away
# #resopnse [4XX] => you screwed up
# #resopnse [5XX] => I screwed up

# #extract json data
# data = response.json()
# longitude = data["iss_position"]['longitude']
# latitude = data['iss_position']['latitude']
# lss_position = (latitude, longitude)
# print(lss_position)

parameters = {
    "lat": 37.51684337188134,
    "lng": 127.03936120321963,
    "formatted":0,
    "tzid":'Asia/Seoul'
}


response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
#?lat=37.51684337188134&lng=127.03936120321963&date=today&tzid=Asia/Seoul
response.raise_for_status()
sunriseandset = response.json()['results']


# def organized_list(timestr):
#     timelist = timestr.split(":")
#     number_ampm_list = timelist[2].split(" ")
#     timelist[2] = number_ampm_list[0]
#     timelist.append(number_ampm_list[1])
#     if timelist[3].upper() == 'PM'.upper():
#         timelist[0] = str(int(timelist[0])+12)
#     del timelist[3]
#     return timelist


sunrise = sunriseandset['sunrise']
sunset = sunriseandset['sunset']
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
hour_now = dt.datetime.now().hour
print(hour_now)
# sunrise_list = organized_list(sunrise)
# sunset_list = organized_list(sunset)

# print(sunrise_list)
# print(sunset_list)

