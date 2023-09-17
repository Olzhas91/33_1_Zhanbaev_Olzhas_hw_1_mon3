from aiogram import types, Dispatcher
from config import bot
from const import START_TEXT, PROFILE_CAPTION_TEXT
from database.sql_commands import Database
from keyboards.Inline_buttons import start_keyboard


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


def register_callback_handlers(dp: Dispatcher):
       dp.register_callback_query_handler(female_answer_call,
                                       lambda call: call.data == 'female_answer')
       dp.register_callback_query_handler(my_profile_call,
                                       lambda call: call.data == 'my_profile')