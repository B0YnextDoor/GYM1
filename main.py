import logging
import filters
from aiogram import Bot, Dispatcher, executor, types
from filters import IsAdminFilter
import configparser

conf = configparser.ConfigParser()
conf.read('config.ini')
logging.basicConfig(level=logging.INFO)
token = conf['bot']['token']
print(token)

bot = Bot(token)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(commands=['start'])
async def start(message):
    await bot.send_message(message.chat.id,'sadasd')


@dp.message_handler(content_types=['new chat members'])
async def on_user_joined(message):
    await message.delete()

@dp.message_handler( commands=['ban'], commands_prefix='!/')
async def cmd_ban(message):
    if message.id == '469522174':
       
        if not message.reply_to_message :
            await message.reply('Эта команда должна быть ответом на сообщение!')
            return
        await message.bot.delete_message(-1001204842425, message.message_id)
        await message.bot.kick_chat_member(-1001204842425, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('БАН НАХУЙ!')


@dp.message_handler()
async def filter_messages(message: types.Message) :
    if 'сука' or 'блядь' in message.text:
        await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp)