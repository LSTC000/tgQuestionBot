import os

from dotenv import load_dotenv
from dotenv import find_dotenv

load_dotenv(find_dotenv())

YOOMONEY_USER_ID = os.getenv('YOOMONEY_USER_ID')
P2P_TOKEN = os.getenv('P2P_TOKEN')

RECEIVER = '4100117963448557'
QUICKPAY_FORM = 'shop'
TARGETS = 'Test'  # Name your application in the YooMoney.
PAYMENT_TYPE = 'SB'
