from os import environ

from dotenv import load_dotenv

load_dotenv()


# configration for the app
class Config:
    MONGO_URI = environ.get("MONGO_URI")
    SECRET_KEY = environ.get("SECRET_KEY")
