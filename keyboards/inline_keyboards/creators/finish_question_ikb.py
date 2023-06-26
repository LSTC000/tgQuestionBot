from data.config import ROW_WIDTH

from data.callbacks import (
    LIKE_CALLBACK_DATA,
    DISLIKE_CALLBACK_DATA,
    REVIEW_CALLBACK_DATA,
    CANCEL_TO_MAIN_MENU_CALLBACK_DATA
)

from data.messages import (
    LIKE_IKB_MESSAGE,
    DISLIKE_IKB_MESSAGE,
    REVIEW_IKB_MESSAGE,
    CANCEL_TO_MAIN_MENU_IKB_MESSAGE
    )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def finish_question_ikb() -> InlineKeyboardMarkup:
    """
    :return: Finish question inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(
        InlineKeyboardButton(text=LIKE_IKB_MESSAGE, callback_data=LIKE_CALLBACK_DATA),
        InlineKeyboardButton(text=DISLIKE_IKB_MESSAGE, callback_data=DISLIKE_CALLBACK_DATA)
    )
    ikb.row(InlineKeyboardButton(text=REVIEW_IKB_MESSAGE, callback_data=REVIEW_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
