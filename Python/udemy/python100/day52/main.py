from instagram import InstaFollower
from dotenv import load_dotenv
import os

load_dotenv()

ID = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

instagram = InstaFollower()

instagram.login(ID, PASSWORD)

instagram.find_followers()

instagram.follow()