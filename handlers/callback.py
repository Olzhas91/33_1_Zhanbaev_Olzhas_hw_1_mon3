import re
import sqlite3

from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT, PROFILE_CAPTION_TEXT
from database.sql_commands import Database
# from keyboards.Inline_buttons import (
#     question_first_keyboard,
#     like_dislike_keyboard,
#     edit_delete_keyboard, register_keyboard,
# )
import random


async def female_answer_call(call: types.CallbackQuery):
    print(call)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='Yes you are female'
    )


async def my_profile_call(call: types.CallbackQuery):
    print(call)
    user = Database().sql_select_user_form_command(
        telegram_id=call.from_user.id
    )

    with open(user[0]['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=PROFILE_CAPTION_TEXT.format(
                nickname=user[0]['nickname'],
                bio=user[0]['bio'],
                age=user[0]['age'],
                occupation=user[0]['occupation'],
                married=user[0]['married'],
            )
        )

async def random_profiles_call(call: types.CallbackQuery):
    user_forms = Database().sql_select_all_user_form_command()
    random_profile = random.choice(user_forms)
    with open(random_profile['photo'], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=PROFILE_CAPTION_TEXT.format(
                nickname=random_profile['nickname'],
                bio=random_profile['bio'],
                age=random_profile['age'],
                occupation=random_profile['occupation'],
                married=random_profile['married'],
            ),
            # reply_markup=await like_dislike_keyboard(
            #     telegram_id=random_profile['telegram_id']
            # )

        )

async def send_complaint_call(call: types.CallbackQuery):
    user_forms = Database().sql_select_user_form_command()


def register_callback_handlers(dp: Dispatcher):
       dp.register_callback_query_handler(female_answer_call,
                                       lambda call: call.data == 'female_answer')
       dp.register_callback_query_handler(my_profile_call,
                                       lambda call: call.data == 'my_profile')
       dp.register_callback_query_handler(random_profiles_call,
                                          lambda call: call.data == 'random_profile')
       dp.register_callback_query_handler(send_complaint_call,
                                          lambda call: call.data == 'send_complaint')