import requests
from datetime import datetime as dt
from datetime import timedelta

#creating account
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "shindig9999"
TOKEN = "shindig8888"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

#creating graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1129381239"
graph_config = {
    "id": graph_id,
    "name": "Coding Study",
    "unit": "Minutes",
    "Type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#generating pixel
now = dt.now().strftime("%Y%m%d")

input_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
input_config = {
    "date": now,
    "quantity": "500.0"
    }

# response = requests.post(url=input_endpoint, json=input_config, headers=headers)
# print(response.text)

#updating pixel
upadte_endpoint = f"{input_endpoint}/{now}"
update_config = {
    "quantity": "500"
}

# response = requests.put(url=update_endpoint, json=update_config, headers= headers)
# print(response.text)

#deleting pixel
yesterday = (dt.now()-timedelta(days=1)).strftime("%Y%m%d")
delete_endpoint = f"{input_endpoint}/{yesterday}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)