from aiogram.dispatcher.filters.state import StatesGroup, State


class PaymentStatesGroup(StatesGroup):
    enter_amount = State()
