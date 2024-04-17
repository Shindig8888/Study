import pandas
import datetime as dt
import random
import smtplib

#global vars
now = dt.datetime.now()
month = now.month
day = now.day
    
#functions
def open_and_write(name_value: str) -> list:
    #open random templates and return with list of letters which [name] is replaced with name of target
    random_letter_number = random.randint(1,3)
    with open(f'letter_templates/letter_{random_letter_number}.txt', 'r') as letter:
        random_letter = letter.read()
        random_letter = random_letter.replace("[NAME]", name_value)
    return random_letter

def send_email(email_value: str, letter: str):
    #send email
    my_email = "calixatexample@gmail.com"
    password = 'stgs szlt fpmm onss'
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=my_email, password=password )
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email_value, 
            msg=f"Subject:Happy birthday!\n\n{letter}"
            )
        

#main
dataframe = pandas.read_csv('birthdays.csv')        
name_list = dataframe[dataframe['month']==month][dataframe['day']==day]['name'].to_list()
email_list = dataframe[dataframe['month']==month][dataframe['day']==day]['email'].to_list()

letters = [open_and_write(name) for name in name_list]
print(letters)

for index in range(0,len(name_list)):
    email = email_list[index]
    letter = letters[index]
    send_email(email, letter)
    





