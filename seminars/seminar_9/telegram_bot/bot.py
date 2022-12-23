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

# Начало программы
max_number = 28
balance_of_candies = 2021

button_hi = KeyboardButton('Привет! 👋')

greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)

button1 = KeyboardButton('1️⃣')
button2 = KeyboardButton('2️⃣')
button3 = KeyboardButton('3️⃣')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Средний ряд'))

button4 = KeyboardButton('4️⃣')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button4, button5)
markup5.insert(button6)


@dp.message_handler(commands=['start2'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.greet_kb)


# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Чтобы ознакомиться с правилами введите: /help")


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer("Игра: На столе лежит 2021 конфета. Играют человек и компьютер "
                         "делая ход друг после друга. Первый ход определяется жеребьёвкой. "
                         "За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента "
                         "достаются сделавшему последний ход.")





# @dp.message_handler(commands=["play"])
# async def cmd_play(message: types.Message):
#     global balance_of_candies
#     move = True





    # while balance_of_candies >= 0:
    # if move:

    # balance_of_candies -= int(message.text)
    # await bot.send_message(message.from_user.id, balance_of_candies)

    # await bot.send_message(message.from_user.id, balance_of_candies)


#         dp.message_handler(commands=["add"])
#         await message.answer("Test 1")
#
#         balance_of_candies-=100
# move, balance_of_candies = moving(player_name_3, move, balance_of_candies, player_color_1)
# else:
# move, balance_of_candies = strong_comp_player(balance_of_candies, move)
# await message.answer(balance_of_candies)
# balance_of_candies -= 28
# await message.answer(balance_of_candies)
# balance_of_candies -= 28


@dp.message_handler(commands=["test1"])
async def cmd_test2(message: types.Message):
    await message.reply("Test 1")


# @dp.message_handler()
# async def cmd_echo(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


# def play():
#     global balance_of_candies
#     move = True
#     while balance_of_candies >= 0:
#         if move:
#             cmd_test_3()
#             balance_of_candies-=1000


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # executor.start_polling(dp)
    asyncio.run(main())
