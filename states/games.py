from aiogram.dispatcher.filters.state import StatesGroup, State


class GamesStatesGroup(StatesGroup):
    game_question = State()
    finish_question = State()
