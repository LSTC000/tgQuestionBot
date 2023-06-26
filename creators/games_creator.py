import os

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.messages import CANCEL_TO_MAIN_MENU_IKB_MESSAGE

from data.config import GAMES_DATA

from data.redis import GAME_NAME_REDIS_KEY, GAME_QUESTION_NUMBER_REDIS_KEY

from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputFile


class GamesCreator:
    async def questions_creator(self, state: FSMContext) -> tuple:
        """
        :param state: FSMContext.
        :return: Question image, question data (text) and questions inline keyboard.
        """

        async with state.proxy() as data:
            game_name = data[GAME_NAME_REDIS_KEY]
            question_number = data[GAME_QUESTION_NUMBER_REDIS_KEY]

        ikb = InlineKeyboardMarkup()

        game_data = GAMES_DATA[game_name]
        question_data = game_data[question_number]

        image = question_data['image']
        answers = question_data['answers']
        question = question_data['question']

        if image is not None:
            for key in image.keys():
                if image[key] is not None:
                    if key == 'path' and os.path.exists(image[key]):
                        image = InputFile(path_or_bytesio=image[key])
                    else:
                        image = image[key]
                    break

        for answer in answers:
            ikb.add(InlineKeyboardButton(text=answer, callback_data=answer))

        ikb.add(
            InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA)
        )

        if question_number:
            question = f'Вопрос {question_number}/{len(game_data) - 1}\n\n{question}'

        return image, question, ikb
