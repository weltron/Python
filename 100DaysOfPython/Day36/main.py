# Importing necessary libraries
import requests
import os
import datetime as dt
import smtplib
from email.message import EmailMessage

# Defining constants and parameters
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_EMAIL = "gt@gmail.com"
MY_PASSWORD =  os.getenv("EMAIL_ACCESS_PASSWORD")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Defining dates for yesterday and the day before yesterday
today = dt.datetime.now()
yesterday = today - dt.timedelta(days=1)
day_before_yesterday = today - dt.timedelta(days=2)

# Fetching stock data from Alpha Vantage API
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("ALPHA_VANTAGE_API_KEY")
}

# Making the API request and processing the stock data
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for key, value in stock_data.items()]

yest_data = stock_data_list[0]
day_before_yest_data = stock_data_list[1]

# Extracting closing prices for yesterday and the day before yesterday
yest_closing_price = float(yest_data["4. close"])
print(yest_closing_price)
day_before_yest_closing_price = float(day_before_yest_data["4. close"])
print(day_before_yest_closing_price)

# Calculating the difference and percentage change in closing prices
diff = round(float(yest_closing_price) - float(day_before_yest_closing_price), 2)
print(diff)

# Determining the direction of stock price movement
up_down = None
if diff > 0:
    up_down = "🔺"
else:    
    up_down = "🔻"

percentage_diff = round((diff / yest_closing_price) * 100, 2)
print(percentage_diff)

# Fetching news articles from News API
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey" : os.getenv("NEWS_API_KEY")
    }
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()
news_data = news_response.json()
articles = news_data["articles"]
top_3_articles = articles[:3]

# Function to send email notifications
def send_email():  
    for article in top_3_articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            msg = EmailMessage()
            msg['Subject'] = f"Stock Alert: {STOCK_NAME} {up_down} {percentage_diff:.2f}%"
            msg['From'] = MY_EMAIL
            msg['To'] = MY_EMAIL        
            msg.set_content(f"Headline: {article['title']}\n\n"
                        f"Brief: {article['description']}")
            connection.send_message(msg)
        
if abs(percentage_diff) > 5:
    send_email()
    print("Email sent successfully!")
else:
    print("No significant change in stock price. No email sent.")