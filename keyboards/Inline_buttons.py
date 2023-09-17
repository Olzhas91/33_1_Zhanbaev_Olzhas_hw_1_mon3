from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

async def start_keyboard():
    markup = InlineKeyboardMarkup()
    form_start_button = InlineKeyboardButton(
        'Регистрация',
        callback_data='fsm_start_form'
    )
    markup.add(
        form_start_button
    )
    return markup

async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    profile_button = InlineKeyboardButton(
        'Мои профиль',
        callback_data='my_profile'
    )

    markup.add(
        profile_button
    )
    return markup

