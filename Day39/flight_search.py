import requests

class FlightSearch():
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
        self.header = "TEQUILA-API-KEY"

    def code_change(self, city):

        parameters = {
            "term" : city['city'],
            "location_types" : "city"
        }
        flight_response = requests.get(url=self.TEQUILA_ENDPOINT, headers=self.header, params=parameters)

        code = flight_response.json()['locations'][0]['code']

        city['iataCode'] = code