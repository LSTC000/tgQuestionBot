from data.config import YOOMONEY_USER_ID

from yoomoney import Authorize


Authorize(
    client_id=YOOMONEY_USER_ID,
    redirect_uri='https://t.me/tgQuestionsBot',  # your bot url.
    scope=[
        'account-info',
        'operation-history',
        'operation-details',
        'incoming-transfers',
        'payment-p2p',
        'payment-shop',
    ]
)
