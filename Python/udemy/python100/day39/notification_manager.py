from twilio.rest import Client
import os
from dotenv import load_dotenv

class NotificationManager:
    def __init__(self) -> None:
        load_dotenv()
        self.account_sid = os.getenv("TWILIO_SID")
        self.auth_token = os.getenv("TWILIO_TOKEN")
        self.client = Client(self.account_sid, self.auth_token)
        self.sender = os.getenv("TWILIO_SENDER")
        self.receiver = os.getenv("TWILIO_RECEIVER")

    def send_flight_message(
            self, 
            price_list, 
            airport_from_list, 
            country_from_name_list,
            airport_to_list,
            country_to_name_list,
            departure_date_list,
            arrival_date_list,
            ): 
        
        for i in range(0, len(price_list)):
            message = self.client.messages.create(
                body=f"Low price alert! Only ₩{price_list[i]} to fly from {country_from_name_list[i]}-{airport_from_list[i]} to {country_to_name_list[i]}-{airport_to_list[i]}, from {departure_date_list[i]} to {arrival_date_list[i]}",
                from_= self.sender,
                to= self.receiver
            )