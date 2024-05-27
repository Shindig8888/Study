from bs4 import BeautifulSoup
import requests
from pprint import pprint
import smtplib
from dotenv import load_dotenv
import os
import time

load_dotenv()

MYEMAIL = os.getenv("MYEMAIL")
PASSWORD = os.getenv("PASSWORD")

merch_url = "https://www.amazon.com/Pattern-Fashion-Packable-Outdoor-Fisherman/dp/B098QT3TMB/ref=sr_1_7?crid=DEPYYJ6MRH0Y&dib=eyJ2IjoiMSJ9.vDXQXv6BjkZ7E1uLCu9yv-1e0iQ5xVvBlYCKIlZEiNoCd8eCUegLnpt-9d05fwhBj8cygrnoq7lU_0DOyo_WJJW80kfZGXZ7J7Kd4gO0hYgTAEsympbNV8W_odQCJS4OFAuAvMX0b7Kghv3Cjx8RimolIEO1uiNBHoTmkvCwGacHB0Uj-Mb2e4SnN9qXfCsI4Ip3IK_DvEcy2cm3T4zcL27ucYsA-crquWFA2xvhl48Zgdit_Wg2ia-EyrEas_9TSFP7ZB8GGln5aUKwQvZSgvZ2_Hc-fCsBf7Sg_bGDGZI.uAL9VPeQ4JeeN_DMVJgNW-huLlKU2C_wTltMAJqTegM&dib_tag=se&keywords=duck&qid=1716779984&sprefix=du%2Caps%2C327&sr=8-7"
header = {
    "Accept-Language":"en-US,en;q=0.9,ko;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url=merch_url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price = float(soup.find(class_="a-section a-spacing-none aok-align-center aok-relative").find(class_="aok-offscreen").string.strip()[1:])
product_name = soup.find(class_="a-size-large product-title-word-break").string.strip()


while True:
    if price <= 14.0:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.login(user=MYEMAIL, password=PASSWORD )
            connection.sendmail(
                from_addr=MYEMAIL, 
                to_addrs="hindig8888@proton.me", 
                msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now ${price}\n\n{merch_url}"
                )
    time.sleep(600)


print(product_name)
pprint(price)