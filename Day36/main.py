import requests
import smtplib
import datetime as dt

MY_EMAIL = "aminaousmanu@gmail.com"
PASSWORD = "PASSWORD"

STOCK_URL = "https://www.alphavantage.co/query"
STOCK_API_KEY = "KEY"
STOCK = "TSLA"

current_date_obj = dt.datetime.now()
pre_date_obj = current_date_obj - dt.timedelta(days=1)
pre_date = pre_date_obj.strftime("%Y-%m-%d")

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_URL, params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]

yesterday_data = stock_data[pre_date]

open_price = yesterday_data["1. open"]
close_price = yesterday_data["4. close"]

stock_price_change = round(((float(close_price) - float(open_price)) / float(open_price)) * 100, 2)


#######################################---NEWS SECTION-----###############################

NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "KEY"
COMPANY_NAME = "TESLA"

news_parameters = {
    "q": COMPANY_NAME,
    "searchIn" : "title",
    "from": pre_date,
    "language": "en",
    "sortBy": "popularity",
    "apiKey" : NEWS_API_KEY,
}


news_response = requests.get(url=NEWS_URL, params=news_parameters)
news_response.raise_for_status()

news_data = news_response.json()

articles = news_data["articles"][:3]


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)

    for i in range (len(articles)):

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="borispokwangeh@gmail.com",
            msg=f"Subject: TESLA: {stock_price_change}% \n\n Headline:{articles[i]['title']}. Brief: {articles[i]['description']} FullStory : {articles[1]['url']}"
        )
