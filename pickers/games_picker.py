from math import ceil

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.config import GAMES_NAME, GAMES_COUNT, GAMES_PICKER_ROW_WIDTH, MAX_GAMES_ON_PAGE

from data.messages import CANCEL_TO_MAIN_MENU_IKB_MESSAGE

from data.redis import PICKER_PAGE_REDIS_KEY

from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class GamesPicker:
    async def games_picker(self, page: int) -> InlineKeyboardMarkup:
        """
        :param page: Current picker page. Start value: 0.
        :return: Inline keyboard for pick a game.
        """

        ikb = InlineKeyboardMarkup(row_width=GAMES_PICKER_ROW_WIDTH)
        ignore_callback = "IGNORE"

        start = page * MAX_GAMES_ON_PAGE
        stop = start + MAX_GAMES_ON_PAGE

        for i in range(start, stop if stop <= GAMES_COUNT else GAMES_COUNT):
            ikb.row(
                InlineKeyboardButton(
                    text=GAMES_NAME[i],
                    callback_data=GAMES_NAME[i]
                )
            )

        ikb.row()
        ikb.insert(
            InlineKeyboardButton(
                text="<<" if page != 0 else " ",
                callback_data="PREV-BRANDS" if page != 0 else ignore_callback
            )
        )
        ikb.insert(
            InlineKeyboardButton(f"{page+1}/{ceil(GAMES_COUNT / MAX_GAMES_ON_PAGE)}", callback_data=ignore_callback)
        )
        ikb.insert(
            InlineKeyboardButton(
                text=">>" if GAMES_COUNT > stop else " ",
                callback_data="NEXT-BRANDS" if GAMES_COUNT > stop else ignore_callback)
        )

        ikb.row(InlineKeyboardButton(CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

        return ikb

    async def process_selection(
            self,
            callback: types.CallbackQuery,
            callback_data: str,
            state: FSMContext
    ) -> tuple:
        """
        :param callback: Callback query the last picker inline keyboard.
        :param callback_data: Callback query data the last picker inline keyboard.
        :param state: FSMContext.
        :return: A tuple consisting of two values: whether the user has chosen a game (Default: False)
        and the name of this game (Default: None).
        """

        async with state.proxy() as data:
            page = data[PICKER_PAGE_REDIS_KEY]

            return_data = False, None

            if callback_data == "IGNORE":
                await callback.answer(cache_time=60)
            elif callback_data == "PREV-BRANDS":
                page -= 1
                data[PICKER_PAGE_REDIS_KEY] = page
                await callback.message.edit_reply_markup(reply_markup=await self.games_picker(page=page))
            elif callback_data == "NEXT-BRANDS":
                page += 1
                data[PICKER_PAGE_REDIS_KEY] = page
                await callback.message.edit_reply_markup(reply_markup=await self.games_picker(page=page))
            elif callback_data != CANCEL_TO_MAIN_MENU_CALLBACK_DATA:
                return_data = True, callback_data

        return return_data
