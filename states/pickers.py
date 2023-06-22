from aiogram.dispatcher.filters.state import StatesGroup, State


class PickersStatesGroup(StatesGroup):
    games_picker = State()
    tests_picker = State()
