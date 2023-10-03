from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from config import bot, DESTINATION_DIR
from database.sql_commands import Database
from keyboards.Inline_buttons import my_profile_keyboard


class FormStates(StatesGroup):
    nickname = State()
    bio = State()
    age = State()
    occupation = State()
    married = State()
    photo =State()

async def fsm_start(call: types.CallbackQuery):
    user = Database().sql_select_user_form_command(
        telegram_id=call.from_user.id
    )
    print(user)
    if user:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text='Ты уже состоишь в Имперской Гвардии. Показать твои данные? ',
            reply_markup=await my_profile_keyboard()
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text='Введите свои никнейм(Позывной)'
        )
        await FormStates.nickname.set()


async def load_nickname(message: types.Message,
                        state: FSMContext):
    async with state.proxy() as data:
        data['nickname'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        'Расскажи о себе немного своему комиссару солдат'
    )


async def load_bio(message: types.Message,
                   state: FSMContext):
    async with state.proxy() as data:
        data['bio'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        'Сколкьо тебе лет солдат? (Только цифры!!!)'
    )


async def load_age(message: types.Message,
                   state: FSMContext):
    try:
        if type(int(message.text)) != int:
            await message.reply(
                text='Ты недотепа! Я же влеел вводить тольок цифры!!! '
                     'давай все заново теперь'
            )
            await state.finish()
        else:
            async with state.proxy() as data:
                data['age'] = message.text
                print(data)
            await FormStates.next()
            await message.reply(
                'Твоя специализация солдат?'
            )
    except ValueError as e:
        await state.finish()
        await message.reply(
            text='Ты недотепа! Я же влеел вводить тольок цифры!!! '
                    'давай все заново теперь'
        )

async def load_occupation(message: types.Message,
                          state: FSMContext):
    async with state.proxy() as data:
        data['occupation'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        'Есть ли у тебя жена или муж боец? Впрочем не важно... можешь поставить прочерк если хочешь -'
    )


async def load_married(message: types.Message,
                       state: FSMContext):
    async with state.proxy() as data:
        data['married'] = message.text
        print(data)
    await FormStates.next()
    await message.reply(
        'Прикрепи фото к личному делу солдат. Отправляйте именно через фото... а не файл!'
    )


async def load_photo(message: types.Message,
                     state: FSMContext):
    print(message.photo)
    path = await message.photo[-1].download(
        destination_dir=DESTINATION_DIR
    )
    async with state.proxy() as data:
        Database().sql_insert_user_form_command(
            telegram_id=message.from_user.id,
            nickname=data['nickname'],
            bio=data['bio'],
            age=data['age'],
            occupation=data['occupation'],
            married=data['married'],
            photo=path.name,
        )
        await message.reply(text='Регистрация прошла успешно солдат теперь ты боец Имперской Гвардии Астра Милитарум')
        await state.finish()

async def send_complaint_button(call: types.CallbackQuery):
    Database().sql_delete_user_form_command(
        telegram_id=call.from_user.id
    )
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You have deleted form successfully"
    )

async def send_complaint_button():
    markup = InlineKeyboardMarkup()
    complaint_button = InlineKeyboardButton(
        'Жалоба',
        callback_data='complaint'
    )

    markup.add(
        complaint_button
    )
    return markup



def register_fsm_form_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(fsm_start,
                                       lambda call: call.data == 'fsm_start_form')
    dp.register_message_handler(load_nickname, state=FormStates.nickname,
                                content_types=['text'])
    dp.register_message_handler(load_bio, state=FormStates.bio,
                                content_types=['text'])
    dp.register_message_handler(load_age, state=FormStates.age,
                                content_types=['text'])
    dp.register_message_handler(load_occupation, state=FormStates.occupation,
                                content_types=['text'])
    dp.register_message_handler(load_married, state=FormStates.married,
                                content_types=['text'])
    dp.register_message_handler(load_photo, state=FormStates.photo,
                                content_types=types.ContentTypes.PHOTO)
    dp.register_callback_query_handler(send_complaint_button,
                                       lambda call: call.data == 'send_complaint_')
