import requests

class DataManager:
    
    def __init__(self) -> None:
        self.URL = "https://sheetdb.io/api/v1/lie2kynwg51hl"
    
    def data_getter(self):
        query = { 'sheet': 'flights' }
        request = requests.get(url=self.URL, json=query)
        request.raise_for_status()
        want_data = request.json()
        return want_data
        

    
