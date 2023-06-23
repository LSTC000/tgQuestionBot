import os

from loader import bot

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.messages import CANCEL_TO_MAIN_MENU_IKB_MESSAGE

from data.config import GAMES_DATA

from data.redis import GAME_NAME_REDIS_KEY, GAME_QUESTION_REDIS_KEY, LAST_IKB_REDIS_KEY

from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile


class GamesCreator:
    async def questions_creator(self, user_id: int, state: FSMContext) -> None:
        """
        :param user_id: Telegram user id.
        :param state: FSMContext.
        :return: None.
        """

        async with state.proxy() as data:
            game_name = data[GAME_NAME_REDIS_KEY]
            game_question = data[GAME_QUESTION_REDIS_KEY]
            data[GAME_QUESTION_REDIS_KEY] += 1

        ikb = InlineKeyboardMarkup()

        question_data = GAMES_DATA[game_name][game_question]

        image = question_data['image']
        answers = question_data['answers']

        if image is not None:
            for key in image.keys():
                if image[key] is not None:
                    if key == 'path' and os.path.exists(image[key]):
                        with open(image[key], 'rb') as file:
                            image = InputFile(file)
                    else:
                        image = image[key]
                    break

        for answer in answers:
            ikb.add(InlineKeyboardButton(text=answer, callback_data=answer))

        ikb.add(
            InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA)
        )

        if image is not None:
            msg = await bot.send_photo(
                chat_id=user_id,
                caption=question_data['question'],
                photo=image,
                reply_markup=ikb
            )
        else:
            msg = await bot.send_message(
                chat_id=user_id,
                text=question_data['question'],
                reply_markup=ikb
            )

        async with state.proxy() as data:
            data[LAST_IKB_REDIS_KEY] = msg.message_id
