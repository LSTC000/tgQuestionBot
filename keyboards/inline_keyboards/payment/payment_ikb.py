from data.config import ROW_WIDTH

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.messages import PAYMENT_URL_IKB_MESSAGE, CANCEL_TO_MAIN_MENU_IKB_MESSAGE

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def payment_ikb(redirected_url: str) -> InlineKeyboardMarkup:
    """
    :param redirected_url: YooMoney redirected url.
    :return: Payment inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=PAYMENT_URL_IKB_MESSAGE, url=redirected_url))
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
