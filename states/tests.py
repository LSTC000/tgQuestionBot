from aiogram.dispatcher.filters.state import StatesGroup, State


class TestsStatesGroup(StatesGroup):
    test_question = State()
    finish_question = State()
    enter_review = State()
