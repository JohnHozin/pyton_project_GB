import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import random

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token='')
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
button10 = KeyboardButton('10')
button11 = KeyboardButton('11')
button12 = KeyboardButton('12')
button13 = KeyboardButton('13')
button14 = KeyboardButton('14')
button15 = KeyboardButton('15')
button16 = KeyboardButton('16')
button17 = KeyboardButton('17')
button18 = KeyboardButton('18')
button19 = KeyboardButton('19')
button20 = KeyboardButton('20')
# button21 = KeyboardButton('21')
# button22 = KeyboardButton('22')
# button23 = KeyboardButton('23')
# button24 = KeyboardButton('24')
# button25 = KeyboardButton('25')
button_new_game = KeyboardButton('Новая игра')

markup = ReplyKeyboardMarkup(row_width=5)
markup.add(button16, button17, button18, button19, button20) \
    .add(button11, button12, button13, button14, button15) \
    .add(button6, button7, button8, button9, button10) \
    .add(button1, button2, button3, button4, button5)

markup2 = ReplyKeyboardMarkup().add(button_new_game)
balance_of_candies_important = 185
balance_of_candies = 185
max_number = 20


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Чтобы ознакомиться с правилами введите: /help", reply_markup=markup2)


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await message.answer(f"Игра: На столе лежит {balance_of_candies} конфет. Играют человек и компьютер "
                         "делая ход друг после друга. Первый ход определяется жеребьёвкой. "
                         f"За один ход можно забрать не более чем {max_number} конфет. Все конфеты оппонента "
                         "достаются сделавшему последний ход.", reply_markup=markup)


@dp.message_handler()
async def process_result(message: types.Message):
    global balance_of_candies
    global balance_of_candies_important
    global max_number
    temp = str(message.date) + " " + str(message.from_user.first_name) + " " + str(
        message.from_user.last_name) + ": " + str(message.text)
    print(temp)
    if message.text == "Новая игра":
        balance_of_candies = balance_of_candies_important
        await message.answer("Осталось: " + str(balance_of_candies) + " конфет", reply_markup=markup)
    elif message.text.isdigit():
        if 1 <= int(message.text) <= max_number:
            if 0 < int(message.text) <= balance_of_candies:
                if message.text == '1':
                    balance_of_candies -= 1
                elif message.text == '2':
                    balance_of_candies -= 2
                elif message.text == '3':
                    balance_of_candies -= 3
                elif message.text == '4':
                    balance_of_candies -= 4
                elif message.text == '5':
                    balance_of_candies -= 5
                elif message.text == '6':
                    balance_of_candies -= 6
                elif message.text == '7':
                    balance_of_candies -= 7
                elif message.text == '8':
                    balance_of_candies -= 8
                elif message.text == '9':
                    balance_of_candies -= 9
                elif message.text == '10':
                    balance_of_candies -= 10
                elif message.text == '11':
                    balance_of_candies -= 11
                elif message.text == '12':
                    balance_of_candies -= 12
                elif message.text == '13':
                    balance_of_candies -= 13
                elif message.text == '14':
                    balance_of_candies -= 14
                elif message.text == '15':
                    balance_of_candies -= 15
                elif message.text == '16':
                    balance_of_candies -= 16
                elif message.text == '17':
                    balance_of_candies -= 17
                elif message.text == '18':
                    balance_of_candies -= 18
                elif message.text == '19':
                    balance_of_candies -= 19
                elif message.text == '20':
                    balance_of_candies -= 20
                # elif message.text == '21':
                #     balance_of_candies -= 21
                # elif message.text == '22':
                #     balance_of_candies -= 22
                # elif message.text == '23':
                #     balance_of_candies -= 23
                # elif message.text == '24':
                #     balance_of_candies -= 24
                # elif message.text == '25':
                #     balance_of_candies -= 25
                if balance_of_candies == 0:
                    await message.answer("Вы выиграли!", reply_markup=markup2)
                else:
                    await message.answer("Осталось конфет: " + str(balance_of_candies), reply_markup=markup)
                    # компьютер
                    if 1 <= balance_of_candies <= max_number:
                        await message.answer(f"Компьютер взял: {str(balance_of_candies)}\n"
                                             f"Компьютер победил!", reply_markup=markup2)
                    else:
                        comp = balance_of_candies % (max_number + 1)
                        if comp == 0:
                            comp = random.randint(1, max_number)
                        balance_of_candies -= comp
                        await message.answer(f"Компьютер взял: {str(comp)}\n"
                                             f"Осталось конфет: {str(balance_of_candies)}", reply_markup=markup)
            else:
                await message.answer("Осталось меньше конфет!\n"
                                     "Осталось конфет: " + str(balance_of_candies), reply_markup=markup)
        else:
            await message.answer(f"Введите число от 1 до {max_number}!", reply_markup=markup)
    else:
        await message.answer(f"Введите число от 1 до {max_number}!", reply_markup=markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # executor.start_polling(dp)
    asyncio.run(main())
