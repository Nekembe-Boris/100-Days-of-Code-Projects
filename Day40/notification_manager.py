import smtplib
import requests


class NotificationManager():
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.EMAIL = "aminaousmanu@gmail.com"
        self.PASSWORD =   "EMAILAUTH"
        self.SHEETY_ENDPOINT_USERS = "https://api.sheety.co/f66da80501983e0aa9e82724ce7fa3fd/flightDeals/users"
        self.response_data = requests.get(url=self.SHEETY_ENDPOINT_USERS)['users']
    
    def send(self, flight_info):
        
        for client in self.response_data[0]:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.login(user=self.EMAIL, password=self.PASSWORD)
                connection.starttls()
                connection.sendmail(
                    from_addr=self.EMAIL,
                    to_addrs=client["email"],
                    msg=f"Subject: Cheap Flights Avalable\n\n Hi {client['firstName']}. Today, we have {flight_info['city']} £{flight_info['price']}"
                )

