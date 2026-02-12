# Importing necessary libraries
import smtplib
import time
import requests
from datetime import datetime

# Constants
MY_LAT = 42.3093241 # Your latitude
MY_LONG = -87.8496551 # Your longitude
MY_EMAIL = "gt@gmail.com"
MY_PASSWORD = "dhfhgfhffffhch"

# Function to check if the ISS is overhead
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Extracting the latitude and longitude of the ISS
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    else:
        return False
    
# Function to check if it is currently dark    
def is_night():
    time_now = datetime.now()
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "America/Chicago",
    }

    # Making a request to the sunrise-sunset API to get the sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True
    else:
        return False 

# Main loop to check the conditions and send an email if necessary
while True:
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
            )
        print("Email sent successfully!")
    else:
        print("The ISS is not overhead or it is not dark yet.")
    time.sleep(60)