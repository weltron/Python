import requests
import os
from datetime import datetime
import json

# Request user input
query = input("What exercise did you do today? ")

# Set up parameters and headers for the exercise API request
exercise_params = {
    "query": query,
}
headers = {
    "x-app-id": os.getenv("APP_ID"),
    "x-app-key": os.getenv("API_KEY"),
}

# Make the API request to get exercise data
response = requests.post(url=os.getenv("EXERCISE_ENDPOINT"), json=exercise_params, headers=headers)
result = response.json()["exercises"][0]

# Set up parameters and headers for the Sheety API request to log the workout
sheety_params = {
    "workout":{
        "date": datetime.now().strftime("%x"),
        "time": datetime.now().strftime("%X"),
        "exercise": result["name"].title(),
        "duration": result["duration_min"],
        "calories": result["nf_calories"]
    }
}

sheety_headers = {
    "Authorization": f"Bearer {os.getenv('SHEETY_BEARER')}"
}

# Make the API request to log the workout in Sheety
sheety_response = requests.post(url=os.getenv("SHEET_ENDPOINT"), json=sheety_params, headers=sheety_headers)
print(sheety_response.text)