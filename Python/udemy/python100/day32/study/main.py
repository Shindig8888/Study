# #email SMTP

# import smtplib

# my_email = "calixatexample@gmail.com"
# password = 'stgs szlt fpmm onss'
# with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
#     connection.login(user=my_email, password=password )
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="calix_example2@yahoo.com", 
#         msg="Subject:Hello\n\nThis is body of my email."
#         )


# import datetime as dt

# now = dt.datetime.now()
# year = now.year
# print(year)

# date_of_birth = dt.datetime(year = 1994, month= 6, day= 5)
# print(date_of_birth)

import random
import smtplib
import datetime as dt


my_email = "calixatexample@gmail.com"
password = 'stgs szlt fpmm onss'

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()

def random_quotes():
    with open('quotes.txt', 'r') as quote_file:
        quotes = quote_file.readlines()
        return quotes
    
def send_email(quote):
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password )
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="calix_example2@yahoo.com", 
            msg=f"Subject:Wednesday Motivation Quote\n\nQuote for {day}/{month}/{year}\n\n{quote}"
            )

    
random_quote = random.choice(random_quotes())
random_ready_quite = random_quote.replace('" -', '"\n\n\t-')
print(random_ready_quite)
if weekday == 2:
    send_email(random_ready_quite)




