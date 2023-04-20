import requests
from twilio.rest import Client

# MY_EMAIL ="frankqqboy12@gmail.com"
# PASSWORD = "bryyyqucazhmakaz"
# receiver_email = "frank851207@gmail.com"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "MD6QXK6MRY9WKUL9"#MD6QXK6MRY9WKUL9
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "0411fd90eb2d480c9534ad7d346f1191"#0411fd90eb2d480c9534ad7d346f1191


TWILIO_SID = "ACac20d360d2c29f16d614794010b4ae13"
TWILIO_TOKEN = "80313c1490b6dafaa84139a101a26529"
TWILIO_PHONE = "+13309698892"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": "TSLA",
    "apikey": STOCK_API,
}

response = requests.get(STOCK_ENDPOINT, params= stock_params)
# print(response.json())
data=response.json()["Time Series (Daily)"]
# print(data)
data_list = [value for (key, value) in data.items()]
data_date = [key for (key, value) in data.items()]
YESTERDAY = data_date[0]
print(YESTERDAY)
yesterday_price = data_list[0]["4. close"]
print(yesterday_price)

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_price = data_list[1]["4. close"]
print(day_before_yesterday_price)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_price = float(yesterday_price) - float(day_before_yesterday_price)
up_down =None
if difference_price > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"
print(difference_price)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
difference_percentage = round((difference_price/float(yesterday_price))*100)
print(difference_percentage)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
news_params = {
    "q" : "Tesla",
    "from" : YESTERDAY,
    "sortBy" : "popularity",
    "apiKey": NEWS_API
}

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(difference_percentage) > 2:
    print("Get News")
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
    # message = [f"Headline: {article['title']}. \n Brief: { article['description']}" for article in three_articles]
    # print(message)

    formatted_articles = [f"TSLA:{up_down}{difference_percentage}% \n " \
                          f"Headline: {article['title']}. \n" \
                          f"Brief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio.
    # with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    #     connection.login(user=MY_EMAIL, password=PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiver_email,
    #                         msg=[f"Headline: {article['title']}. \n Brief: { article['description']}" for article in three_articles])
    client = Client(TWILIO_SID, TWILIO_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(body=article, from_='+13309698892', to='+17788981207')
        print(message)
#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

