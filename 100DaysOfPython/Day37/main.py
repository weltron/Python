import requests
import os
from datetime import datetime, timedelta

# 1. Create a user account
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response =requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# 2. Create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Minutes",
    "type": "int",
    "color": "sora",
    "timezone": "America/Chicago"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# 3. Post a pixel
pixela_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}

response = requests.post(url=pixela_endpoint, json=pixel_params, headers=headers)
print(response.text)

# 4. Update a pixel
update_endpoint = f"{pixela_endpoint}/{today.strftime('%Y%m%d')}"

update_params = {
    "quantity": "125",
}

# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

yesterday = today - timedelta(days=1)

# 5. Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{yesterday.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)