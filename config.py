from decouple import config
from aiogram import Bot, Dispatcher

TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)
ADMIN_ID = 574359438
GROUP_ID = -1001841384302
