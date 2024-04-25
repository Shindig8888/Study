

class FlightData:
    def __init__(self):
        self.price_list = []
        self.country_from_name_list = []
        self.airport_from_list = []
        self.country_to_name_list = []
        self.airport_to_list = []
        self.departure_date_list = []
        self.arrival_date_list = []

    def gen_data(self, flgiht_json):
        for search in flgiht_json:
            for another_item in search["data"]:
                arrival_date = another_item['route'][-1]['local_departure'].split("T")[0]
                self.arrival_date_list.append(arrival_date)
                departure_date = another_item['route'][0]['local_departure'].split("T")[0]
                self.departure_date_list.append(departure_date)
                price = another_item["price"]
                self.price_list.append(price)
                country_from = another_item['route'][0]['cityFrom']
                self.country_from_name_list.append(country_from)
                airport_from = another_item['route'][0]['flyFrom']
                self.airport_from_list.append(airport_from)
                country_to = another_item['route'][0]['cityTo']
                self.country_to_name_list.append(country_to)
                airport_to = another_item['route'][0]['flyTo']
                self.airport_to_list.append(airport_to)

                

                

    #This class is responsible for structuring the flight data.
    pass