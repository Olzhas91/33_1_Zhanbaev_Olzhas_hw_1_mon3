from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 574359438
GROUP_ID = -1001841384302
DESTINATION_DIR = 'C:/Users/User/Desktop/3-MonPY3.8/media'
