from api_requests import APIRequests
STOCK = "AMD"
COMPANY_NAME = "AMD"

api = APIRequests()
data = api.get_stock_data(STOCK)
market_dates = list(data.keys())
closing_prices = [float(data[key]["4. close"]) for key in market_dates[:2]]


def check_stocks():
    sorted_prices = sorted(closing_prices)
    high = sorted_prices[1]
    low = sorted_prices[0]
    change = (high - low) / low

    if high == closing_prices[0]:
        up_down = "📈"
    else:
        up_down = "📉"

    # Send messages with news title and description
    if change >= 0.05:
        news_response = api.get_news_articles(COMPANY_NAME)["articles"][:3]
        news_title_desc = [[item["title"], item["description"]] for item in news_response]
        for t_d in news_title_desc:
            api.send_telegram_message(f'{STOCK} {up_down} {round(change * 100)}%\n{t_d[0]}\n{t_d[1]}')


check_stocks()

# import requests
# import os
# from dotenv import load_dotenv
#
# load_dotenv("F:/random/.env")
# chat_id = os.getenv("chat_id")
# telegram_api = os.getenv("telegram_weather_api")
#
# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"
#
# # Stock API and information
# av_api = "C2YJF7PJAYOV1ULD"
# parameters = {
#     "function": "TIME_SERIES_DAILY_ADJUSTED",
#     "symbol": STOCK,
#     "apikey": av_api,
# }
# url = 'https://www.alphavantage.co/query'
# r = requests.get(url, params=parameters)
# data = r.json()["Time Series (Daily)"]
# market_dates = list(data.keys())
# closing_prices = [float(data[key]["4. close"]) for key in market_dates[:2]]
#
# # Stock news API and information
# news_api = "9d8b51824f8a4aba8b6571520705ed75"
# news_params = {
#     "q": COMPANY_NAME,
#     "from": market_dates[0],
#     "sortBy": "popularity",
#     "language": "en",
#     "apiKey": news_api,
# }
# news_url = 'https://newsapi.org/v2/everything'
#
#
# def check_stocks():
#     sorted_prices = sorted(closing_prices)
#     if sorted_prices[0] == closing_prices[0]:
#         up_down = "📉"
#     else:
#         up_down = "📈"
#
#     high = sorted_prices[1]
#     low = sorted_prices[0]
#     change = (high - low) / low
#
#     # Send messages with news title and description
#     if change >= 0.01:
#         news_response = requests.get(news_url, params=news_params).json()["articles"][:3]
#         news_title_desc = [[item["title"], item["description"]] for item in news_response]
#         for t_d in news_title_desc:
#             telegram_bot_sendtext(f'{STOCK} {up_down} {round(change * 100)}%\n{t_d[0]}\n{t_d[1]}')
#
#
# def telegram_bot_sendtext(bot_message):
#     send_text = 'https://api.telegram.org/bot' + telegram_api + '/sendMessage?chat_id=' + chat_id + \
#                 '&parse_mode=Markdown&text=' + bot_message
#     requests.get(send_text)
#
#
# check_stocks()
