from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminMenuStatesGroup(StatesGroup):
    admin_menu = State()
    alert_for_users = State()
    confirm_for_users = State()
