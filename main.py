import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
stock_api = os.getenv("STOCK_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
sms_no = os.getenv("SMS_NO")
whatsapp_no = os.getenv("WHATSAPP_NO")
user_no = os.getenv("USER_NO")

STOCK = "IBM"
COMPANY_NAME = "IBM"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "demo"
}
stock_info = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
markets = stock_info.json()["Time Series (Daily)"]
dates = markets.keys()
yesterday = list(dates)[0]
dayBefore = list(dates)[1]

closing_price_yesterday = float(markets[yesterday]['4. close'])
closing_price_dayBefore = float(markets[dayBefore]['4. close'])

difference = abs(closing_price_yesterday-closing_price_dayBefore)
percent = (difference/closing_price_yesterday) * 100


news_params = {
    "apiKey": news_api_key,
    "q": "ibm",
    "pageSize": 3,
}
stock_news = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
stock_news_list = stock_news.json()['articles']


for i in stock_news_list:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Difference: {percent}%\n\nTitle: {i['title']}\n\n{i['description']}",
        from_=sms_no,
        to=user_no
    )
    print(message.status)
    message1 = client.messages.create(
        body=f"Difference: {percent}%\n\nTitle: {i['title']}\n\n{i['description']}",
        from_=f'whatsapp:{whatsapp_no}',
        to=f'whatsapp:{user_no}'
    )
    print(message1.status)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

