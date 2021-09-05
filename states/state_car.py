from aiogram.dispatcher.filters.state import StatesGroup, State


class State_celect(StatesGroup):
    select_category = State()


class get_update_url_drom(StatesGroup):
    update_url = State()
