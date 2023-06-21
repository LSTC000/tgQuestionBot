from data.config import ROW_WIDTH

from data.callbacks import START_CALLBACK_DATA

from data.messages import START_IKB_MESSAGE

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_ikb() -> InlineKeyboardMarkup:
    """
    :return: Start command inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=START_IKB_MESSAGE, callback_data=START_CALLBACK_DATA))

    return ikb
