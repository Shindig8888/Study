

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
        for item in flgiht_json:
            root = item["data"]
            for another_item in root:
                try:
                    arrival_date = another_item['route'][1]['local_departire'].split["T"]
                    self.arrival_date_list(arrival_date)

                    departure_date = another_item['route'][0]['local_departire'].split["T"]
                    self.departure_date_list(departure_date)

                    price = another_item['price']
                    self.price_list.append(price)

                    country_from = another_item['cityFrom']
                    self.country_from_name_list.append(country_from)
                    airport_from = another_item['flyFrom']
                    self.airport_from_list.append(airport_from)

                    country_to = another_item['cityTo']
                    self.country_to_name_list.append(country_to)
                    airport_to = another_item['flyTo']
                    self.airport_to_list.append(airport_to)

                except IndexError:
                    pass
                except KeyError:
                    pass

                

    #This class is responsible for structuring the flight data.
    pass