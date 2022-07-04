ttt = "5359762951:AAGZCgSwJk3GqkQOTtLxUs_OheOiWyIktR4"
Group_ID=1
import logging
import filters

from aiogram import Bot, Dispatcher, executor, types
from filters import IsAdminFilter
logging.basicConfig(level=logging.INFO)

bot = Bot(token=ttt)
dp = Dispatcher(bot)

dp.filters_factory.bind(IsAdminFilter)

@dp.message_handler(content_types=['new chat members'])
async def on_user_joined(message):
    await message.delete()

@dp.message_handler( commands=['ban'], commands_prefix='!/')
async def cmd_ban(message):
    # if message.id == 'твой id':
    #     pass
    if not message.reply_to_message :
        await message.reply('Эта команда должна быть ответом на сообщение!')
        return
    await message.bot.delete_message(Group_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=Group_ID, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply('БАН НАХУЙ!')
@dp.message_handler()
async def filter_messages(message: types.Message) :
    if 'сука' or 'блядь' in message.text:
        await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates= True)