import os

from data.callbacks import (
    LIKE_CALLBACK_DATA,
    DISLIKE_CALLBACK_DATA,
    REVIEW_CALLBACK_DATA,
    CANCEL_TO_MAIN_MENU_CALLBACK_DATA,
)

from data.messages import LIKE_IKB_MESSAGE, DISLIKE_IKB_MESSAGE, REVIEW_IKB_MESSAGE, CANCEL_TO_MAIN_MENU_IKB_MESSAGE

from data.config import GAMES_DATA, ROW_WIDTH

from data.redis import GAME_NAME_REDIS_KEY, GAME_QUESTION_NUMBER_REDIS_KEY, USER_ANSWERS_REDIS_KEY

from utils import AnswerFinder

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

        ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

        game_data = GAMES_DATA[game_name][0]
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

    async def finish_creator(self, state: FSMContext) -> tuple:
        """
        :param state: FSMContext.
        :return: Answer description, image answer if it exists and finish inline keyboard.
        """

        async with state.proxy() as data:
            game_data = GAMES_DATA[data[GAME_NAME_REDIS_KEY]][1]
            finder_method = game_data['finder_method']

            if finder_method == 'best_weight':
                answer = game_data[AnswerFinder().best_weight(data[USER_ANSWERS_REDIS_KEY])]
                description = answer['description']

        image = answer['image']

        if image is not None:
            for key in image.keys():
                if image[key] is not None:
                    if key == 'path' and os.path.exists(image[key]):
                        image = InputFile(path_or_bytesio=image[key])
                    else:
                        image = image[key]
                    break

        ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

        ikb.row(
            InlineKeyboardButton(text=LIKE_IKB_MESSAGE, callback_data=LIKE_CALLBACK_DATA),
            InlineKeyboardButton(text=DISLIKE_IKB_MESSAGE, callback_data=DISLIKE_CALLBACK_DATA)
        )
        ikb.row(InlineKeyboardButton(text=REVIEW_IKB_MESSAGE, callback_data=REVIEW_CALLBACK_DATA))
        ikb.row(
            InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA)
        )

        return image, description, ikb
