import requests
from datetime import datetime, timedelta
import pytz
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api = "8RN39XR7EI40NWFN"
news_api = "6d3248cab53e44ec8017b49019c92e94"

# ## STEP 1: Use https://www.alphavantage.co
# # When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# request = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=7E5APZI1KCT5AVNE')
# request.raise_for_status()
# data = request.json()
# print(data)

now_utc = datetime.now(pytz.utc)

day_yester = now_utc-timedelta(days=1)
day_before_yester = now_utc-timedelta(days=2)

weekday_now = now_utc.weekday()

# if weekday_now==0:
#     day_yester = now_utc-timedelta(days=3)
#     day_before_yester = now_utc-timedelta(dasy=4)
# elif weekday_now==1:
#     day_before_yester = now_utc-timedelta(days=4)
# elif weekday_now==6:
#     day_yester = now_utc-timedelta(days=2)
#     day_before_yester = now_utc-timedelta(days=3)

# close_yesterday:float = float(data['Time Series (Daily)'][str(day_yester).split(" ")[0]]['4. close'])
# close_before_yesterday:float = float(data['Time Series (Daily)'][str(day_before_yester).split(" ")[0]]['4. close'])
# print(close_yesterday)
# print(close_before_yesterday)
# uprise:float = (1-close_yesterday/close_before_yesterday)*100

uprise = 8.0



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news = requests.get(f'https://newsapi.org/v2/top-headlines?country=us&q=tesla&from={str(day_before_yester).split(" ")[0]}&sortBy=popularity&apiKey=6d3248cab53e44ec8017b49019c92e94')
news.raise_for_status()
news_data = news.json()

news_headline = []
news_brief = []
try:
    for n in range(0,3):
        news_headline.append(news_data['articles'][n]['title'])
        news_brief.append(news_data['articles'][n]['title'])
except IndexError:
    pass

print(news_headline)
print(news_brief)
    

if uprise >= 5.0:
    sms_stock = f"{STOCK}: 🔺{round(uprise, 2)}%"
elif uprise <= -5.0:
    sms_stock = f"{STOCK}: 🔻{round(uprise, 2)}%"

client = Client("AC565f15f515bb34c6240ff6815d0a8f2d", "464411313bc035473019e8b5996b13a3")
for n in range(0, len(news_headline)):
    message = client.messages.create(
        body=f"{sms_stock}\nHeadline: {news_headline[n]}\nBrief: {news_brief[n]}",
        from_="+12513330579",
        to="+821033393818"
    )
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

