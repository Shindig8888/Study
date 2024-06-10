from dotenv import load_dotenv
import os
from twitbot import InternetSpeedTwitterBot

load_dotenv()
PROMISED_DOWN = 120
PROMISED_DOWN = 100
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASS = os.getenv("PASS")

bot = InternetSpeedTwitterBot()

# bot.get_internet_speed()

bot.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASS)