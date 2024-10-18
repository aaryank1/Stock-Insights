# Stock Market and News Notifier

This Python project provides real-time updates on stock price movements and fetches related news articles. It uses Twilio's messaging services to send SMS and WhatsApp notifications whenever there's a significant price change in the stock. Additionally, it retrieves top news articles related to the stock using the NewsAPI.

## Features
- Fetches daily stock prices for the specified stock.
- Calculates the percentage difference between the latest two closing prices.
- Fetches the latest news articles related to the company from NewsAPI.
- Sends SMS and WhatsApp notifications to the user with stock price changes and news details using Twilio.

## Requirements
- Python 3.x
- Twilio Account
- Alpha Vantage API key
- NewsAPI key

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/stock-market-notifier.git
   cd stock-market-notifier

   ```bash
   pip install requests python-dotenv twilio

ACCOUNT_SID=<Your Twilio Account SID>
AUTH_TOKEN=<Your Twilio Auth Token>
STOCK_API_KEY=<Your Alpha Vantage API Key>
NEWS_API_KEY=<Your NewsAPI Key>
SMS_NO=<Your Twilio SMS Number>
WHATSAPP_NO=<Your Twilio WhatsApp Number>
USER_NO=<Recipient Phone Number>

STOCK = "IBM"  # Change this to your preferred stock
COMPANY_NAME = "IBM"

## How It Works
------------

1.  The script fetches daily stock data using Alpha Vantage's API.
2.  It calculates the percentage difference between the closing prices of the last two trading days.
3.  If there is a significant price change, the script fetches the top 3 news articles related to the company from NewsAPI.
4.  The articles and price difference are sent to the user via SMS and WhatsApp using Twilio.
