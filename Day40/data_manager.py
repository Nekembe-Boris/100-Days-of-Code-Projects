import requests


class DataManager():
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_ENDPOINT_GET = "https://api.sheety.co/f66da80501983e0aa9e82724ce7fa3fd/flightDeals/prices"
        self.response_data = requests.get(url=self.SHEETY_ENDPOINT_GET)

    def response(self):
        prices = self.response_data.json()["prices"]
        return prices

    def put_code(self, data):
        row_id = 2
        for i in range(len(data)):
            PUT_ENDPOINT = f"https://api.sheety.co/f66da80501983e0aa9e82724ce7fa3fd/flightDeals/prices/{row_id}"
            info = {
                "price" : {
                    "iataCode" : data[i]["iataCode"]
                }
            }
            response = requests.put(url=PUT_ENDPOINT, json=info)
            row_id  += 1


class NewUsers():
    #This class adds new users to the USERS sheet on google.
    def __init__(self):
        self.USERS_POST_ENDPOINT = "https://api.sheety.co/f66da80501983e0aa9e82724ce7fa3fd/flightDeals/users"
        welcome = print("Welcome to Boris' Flight Club\nGet the best flight deals ever in your email")
        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?]\n")
        self.email = input("What is your email address?\n")
        self.verify = input("Type your email again!\n")


    def register(self):
        """This function registers new members to our USERS sheet"""
        if self.verify == self.email:
            details = {
                "user" : {
                    'firstName' : self.first_name,
                    'lastName' : self.last_name,
                    'email' : self.email
                }
            }
            register_response = requests.post(url=self.USERS_POST_ENDPOINT, json=details)
