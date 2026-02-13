import requests
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
import os

# Define your latitude and longitude coordinates for your location
MY_LATITUDE = 40.059958
MY_LONGITUDE = -5.755753

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}

# Get your OpenWeatherMap API key and Twilio credentials from environment variables
api_key = "[API KEY]" #os.environ.get("OWM_API_KEY")
account_sid = "[ACCOUNT_SID]"
auth_token = "[AUTH_TOKEN]" #os.environ.get("TWILIO_AUTH_TOKEN")

# Set up the parameters for the API request to OpenWeatherMap
parameters = {
    "lat": MY_LATITUDE, 
    "lon": MY_LONGITUDE,
    "appid": api_key,
     "cnt": 4,
}

# Make the API request to OpenWeatherMap and check if it will rain in the next 12 hours
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

# Check the weather condition codes for the next 4 hours (12 hours total) to see if it will rain.
# Weather condition codes less than 700 indicate rain.
will_rain = False
for hour in weather_data["list"]:
    condition = hour["weather"][0]["id"]
    if condition < 700:
        will_rain = True

# If it will rain, send a text message using Twilio to remind you to carry an umbrella.      
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18444734145',
        body='It\'s gonna rain today. Be sure to carry an umbrella.',
        to='+15052368016'
    )
    print(message.sid)
    print(message.status)
