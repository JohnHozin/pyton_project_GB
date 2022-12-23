import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import bot_token as bt

from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=bt.token)
# Диспетчер
dp = Dispatcher(bot)

button1 = KeyboardButton('1')
button2 = KeyboardButton('2')
button3 = KeyboardButton('3')
button4 = KeyboardButton('4')
button5 = KeyboardButton('5')
button6 = KeyboardButton('6')
button7 = KeyboardButton('7')
button8 = KeyboardButton('8')
button9 = KeyboardButton('9')

markup = ReplyKeyboardMarkup().add(button1).add(button2).add(button3).add(button4).add(button5).add(button6).add(
    button7).add(button8).add(button9)
markup3 = ReplyKeyboardMarkup().row(button1, button2, button3).row(button4, button5, button6).row(button7, button8,
                                                                                                  button9)





@dp.message_handler(commands=['start1'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=markup3)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Чтобы ознакомиться с правилами введите: /help")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # executor.start_polling(dp)
    asyncio.run(main())
