import requests

class DataManager:
    
    def __init__(self) -> None:
        self.URL = "https://sheetdb.io/api/v1/oqzqu0z4m2v6d"
    
    def data_getter(self):
        request = requests.get(url=self.URL)
        request.raise_for_status()
        want_data = request.json()
        return want_data
        

    
