import requests
import datetime as dt

today = dt.datetime.now()
date_to_obj = today + dt.timedelta(days=180)
return_from_obj = today + dt.timedelta(days=7)
return_to_obj = today + dt.timedelta(days=28)


class FlightData():
        #This class is responsible for structuring the flight data and returning a list of cities and the various prices.
    def __init__(self):
        self.SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
        self.header = "TEQUILA-API-KEY"
        self.cur_location = "LON"
        self.date_from = today.strftime("%d/%m/%Y")
        self.date_to = date_to_obj.strftime("%d/%m/%Y")
        self.return_from = return_from_obj.strftime("%d/%m/%Y")
        self.return_to = return_to_obj.strftime("%d/%m/%Y")
        self.currency = "GBP"

    def flight_search(self, data):

        for i in range(len(data[0])):
            try:
                search_info = {
                    "fly_from": self.cur_location,
                    "fly_to" : data[i]['iataCode'],
                    "date_from" : self.date_from,
                    "date_to " : self.date_to,
                    "return_from" : self.return_from,
                    "return_to" : self.return_to,
                    "curr" : self.currency,
                    "price_to" : data[i]['lowestPrice']
                }
            except TypeError:
                print("No data")
            else:
                flight_price_response = requests.get(url=self.SEARCH_ENDPOINT, headers=self.header, params=search_info)
                flight_price_response.raise_for_status()

                flight_data = flight_price_response.json()['data']

                print(flight_data)

                cheap_flights = []

                if len(flight_data) > 0:

                    price = flight_data[0]['price']
                    city = flight_data[0]['cityTo']

                cheap_flights.append({city : f"{self.currency} {price}"})
        return cheap_flights
