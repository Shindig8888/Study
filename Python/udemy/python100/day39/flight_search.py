import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt
from datetime import timedelta



class FlightSearch:
    def __init__(self) -> None:
        self.URL = "https://tequila-api.kiwi.com/v2/search"
        self.CURRENCY = "KRW"
        self.FLIGHT_FROM = "ICN"
        self.date_from = str(dt.now().strftime("%d/%m/%Y"))
        self.date_to = str((dt.now() + timedelta(days=180)).strftime("%d/%m/%Y"))
        

    def search(self, flight_to_list, max_price_list):
        flight_data = []
        load_dotenv()
        for number in range(0, len(flight_to_list)):
            headers = {
                "apikey": os.getenv("KIWIAPI_KEY")
            }

            parameters = {
                "fly_from": self.FLIGHT_FROM,
                "fly_to": flight_to_list[number],
                "date_from": self.date_from,
                "date_to": self.date_to,
                "curr": self.CURRENCY,
                "price_from": "150000",
                "price_to": str(max_price_list[number]),
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "one_for_city": 1,
                "max_stopovers": 0
            }
                
            
            response = requests.get(url=self.URL, params=parameters, headers=headers)
            flight_data.append(response.json())
        return flight_data
        



    #This class is responsible for talking to the Flight Search API.
    pass