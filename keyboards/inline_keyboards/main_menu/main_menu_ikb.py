from data.config import ROW_WIDTH

from data.callbacks import (
    GAMES_PICKER_CALLBACK_DATA,
    TESTS_PICKER_CALLBACK_DATA,
    CHANGE_ALERT_CALLBACK_DATA
)

from data.messages import (
    GAMES_PICKER_IKB_MESSAGE,
    TESTS_PICKER_IKB_MESSAGE,
    ALERT_ON_IKB_MESSAGE,
    ALERT_OFF_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_ikb(alert: bool) -> InlineKeyboardMarkup:
    """
    :param alert: True if the user has enabled alerts, else False.
    :return: Main menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=GAMES_PICKER_IKB_MESSAGE, callback_data=GAMES_PICKER_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=TESTS_PICKER_CALLBACK_DATA, callback_data=TESTS_PICKER_IKB_MESSAGE))
    ikb.row(InlineKeyboardButton(
        text=ALERT_OFF_IKB_MESSAGE if alert else ALERT_ON_IKB_MESSAGE,
        callback_data=CHANGE_ALERT_CALLBACK_DATA)
    )

    return ikb
