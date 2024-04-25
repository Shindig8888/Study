from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import json

data = DataManager()



want_flight = data.data_getter()
city_list = []
flight_to_list = []
low_price_list = []

for number in range(0, len(want_flight)):
    city_list.append(want_flight[number]['City'])
    flight_to_list.append(want_flight[number]['IATA Code'])
    low_price_list.append(want_flight[number]['Lowest Price'])

print(city_list)
print(flight_to_list)
print(low_price_list)

flight_searcher = FlightSearch()
flight_data = flight_searcher.search(flight_to_list=flight_to_list, max_price_list=low_price_list)

with open("data.json", "w") as json_file:
    json.dump(flight_data, json_file)

flight_catcher = FlightData()
flight_catcher.gen_data(flight_data)

flight_catcher.price_list,
flight_catcher.airport_from_list,
flight_catcher.country_from_name_list,
flight_catcher.airport_to_list,
flight_catcher.country_to_name_list,
flight_catcher.departure_date_list,
flight_catcher.arrival_date_list,

smssender = NotificationManager()
smssender.send_flight_message(
    flight_catcher.price_list,
    flight_catcher.airport_from_list,
    flight_catcher.country_from_name_list,
    flight_catcher.airport_to_list,
    flight_catcher.country_to_name_list,
    flight_catcher.departure_date_list,
    flight_catcher.arrival_date_list
)


