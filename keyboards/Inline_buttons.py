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
    random_profiles_button = InlineKeyboardButton(
        'Просмотреть пользователей',
        callback_data='random_profile'
    )
    referral_button = InlineKeyboardButton(
        'Реферальное меню',
        callback_data='referral_menu'
    )
    markup.add(
        form_start_button
    ).add(
        random_profiles_button
    ).add(
        referral_button
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

async def like_dislike_keyboard(telegram_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        '👍🏻',
        callback_data=f'_like_{telegram_id}'
    )
    dislike_button = InlineKeyboardButton(
        '👎🏻',
        callback_data='random_profile'
    )
    markup.add(
        like_button
    ).add(
        dislike_button
    )
    return markup

async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    reference_link_button = InlineKeyboardButton(
        'Сгенерировать ссылку',
        callback_data='reference_link'
    )
    reference_list_button = InlineKeyboardButton(
        'Список рефералов',
        callback_data='reference_list'
    )
    markup.add(
        reference_link_button
    ).add(
        reference_list_button
    )
    return markup