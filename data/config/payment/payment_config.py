import os

from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

PAYMENT_TOKEN = os.getenv('PAYMENT_TOKEN')

PAYMENT_TITLE = 'Поддержка проекта'
PAYMENT_DESCRIPTION = 'Все полученные средства уйдут на развитие проекта.'
