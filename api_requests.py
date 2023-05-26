import requests
import os
from dotenv import load_dotenv
import json


class APIRequests:
    def __init__(self):
        load_dotenv("F:/random/.env")

    def send_telegram_message(self, message):
        chat_id = os.getenv("chat_id")
        telegram_api = os.getenv("telegram_weather_api")
        send_text = 'https://api.telegram.org/bot' + telegram_api + '/sendMessage?chat_id=' + chat_id + \
                    '&parse_mode=Markdown&text=' + message
        return requests.get(send_text)

    def get_stock_data(self, stock_symbol):
        av_api = os.getenv("alphavantage_api_key")
        parameters = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": stock_symbol,
            "apikey": av_api,
        }
        url = 'https://www.alphavantage.co/query'
        return requests.get(url, params=parameters).json()["Time Series (Daily)"]

    def get_news_articles(self, query):
        news_api = os.getenv("newsapi_api_key")
        news_params = {
            "q": query,
            "sortBy": "popularity",
            "language": "en",
            "apiKey": news_api,
        }
        news_url = 'https://newsapi.org/v2/everything'
        return requests.get(news_url, params=news_params).json()

    def print_json_structure(self, json_response):
        formatted_response = json.dumps(json_response, indent=2)
        print(formatted_response)


# api = APIRequests()
# api.print_json_structure(api.get_stock_data("AMD"))
