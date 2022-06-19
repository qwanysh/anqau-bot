import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

DATABASE_URL = os.getenv('DATABASE_URL')

ANQAU_USER_ID = int(os.getenv('ANQAU_USER_ID'))

HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')

HEROKU_PORT = os.getenv('PORT')
