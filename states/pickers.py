from aiogram.dispatcher.filters.state import StatesGroup, State


class PickersStatesGroup(StatesGroup):
    games_picker = State()
