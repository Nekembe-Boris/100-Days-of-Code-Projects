import requests
import datetime as dt

TOKEN = "TOKEN"
USERNAME =  "kirkcaves"

date = dt.datetime(year=2023, month=9, day=12)



######################Creating a user####################
CREATE_USER_ENDPOINT = "https://pixe.la/v1/users"
create_user_parameters = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}
response = requests.post(url=CREATE_USER_ENDPOINT, json=create_user_parameters)



###########Create graph###############
CREATE_G_ENDPOINT = f"{CREATE_USER_ENDPOINT}/{USERNAME}/graphs"

graph_parameters = {
    "id" : "graph1",
    "name" : "Code Tracker",
    "unit" : "min",
    "type" : "int",
    "color": "shibafu"
}

header = {
    "X-USER-TOKEN" : TOKEN
}

graph_response = requests.post(url=CREATE_G_ENDPOINT, json=graph_parameters, headers=header)




###########Adding pixel to a graph###################
POST_DATA_ENDPOINT = f"{CREATE_G_ENDPOINT}/{graph_parameters['id']}"

post_data_params = {
    "date" : date.strftime("%Y%m%d"),
    "quantity" : "20"
}

post_response = requests.post(url=POST_DATA_ENDPOINT, json=post_data_params, headers=header)



############# Updating a pixel########################
UPDATE_PIXEL_ENDPOINT = f"{POST_DATA_ENDPOINT}/{post_data_params['date']}"

update_params = {
    "quantity" : "150"
}

update_response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_params, headers=header)



##############Delete a pixel##############
DELETE_ENDPOINT = f"{UPDATE_PIXEL_ENDPOINT}"

delete_response = requests.delete(url=DELETE_ENDPOINT, headers=header)
