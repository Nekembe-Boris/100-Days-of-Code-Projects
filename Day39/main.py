import requests
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData


data = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

sheet_data = data.response()

#changes the iataCode in the sheetdata to the correct code obtained from the api response
try:
    for city in sheet_data:
        flight_search.code_change(city)
except TypeError:
    print("No data")



#writes the IATA Code culumn in our PRICES sheet
write_to_sheet = data.put_code(data=sheet_data)

#INFO variable will be a dictionary of available cities and the various prices nested in a list
info = flight_data.flight_search(sheet_data)






# print(info)