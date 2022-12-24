import asyncio
import logging
from aiogram import Bot, Dispatcher, types
import bot_token as bt

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

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
button0 = KeyboardButton('0')
button_add = KeyboardButton('+')
button_sub = KeyboardButton('-')
button_mult = KeyboardButton('*')
button_div = KeyboardButton('/')
button_res = KeyboardButton('=')
button_del = KeyboardButton('c')

markup = ReplyKeyboardMarkup(row_width=4)
markup.add(button7, button8, button9, button_div) \
    .add(button4, button5, button6, button_mult) \
    .add(button1, button2, button3, button_sub) \
    .add(button0, button_del, button_res, button_add)

value = ""
num_1 = 0
option = ""
result = 0
filePath = '/text.txt'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Калькулятор запущен!"
                         "Ознакомиться с принципом работы /help", reply_markup=markup)


@dp.message_handler(commands=['help'])
async def process_start_command(message: types.Message):
    await message.answer("Ввод производится через меню или с клавиатуры по одной цифре или символу."
                         "Калькулятор считает только одно действие, примеры:"
                         " 2 + 2 = 4, 5 * 5 = 25, 6 / 3 = 2", reply_markup=markup)


@dp.message_handler()
async def process_result(message: types.Message):
    global value
    global num_1
    global option
    global result
    if message.text == '1':
        value += '1'
    elif message.text == '2':
        value += '2'
    elif message.text == '3':
        value += '3'
    elif message.text == '4':
        value += '4'
    elif message.text == '5':
        value += '5'
    elif message.text == '6':
        value += '6'
    elif message.text == '7':
        value += '7'
    elif message.text == '8':
        value += '8'
    elif message.text == '9':
        value += '9'
    elif message.text == '0':
        if value != "":
            value += '0'
    elif message.text == '+':
        if value == "":
            await message.answer('Ошибка', reply_markup=markup)
        else:
            num_1 = int(value)
            option = "+"
            value = ""
            await message.answer(f'{num_1} {option} ', reply_markup=markup)
    elif message.text == '-':
        if value == "":
            await message.answer('Ошибка', reply_markup=markup)
        else:
            num_1 = int(value)
            option = "-"
            value = ""
            await message.answer(f'{num_1} {option} ', reply_markup=markup)
    elif message.text == '*':
        if value == "":
            await message.answer('Ошибка', reply_markup=markup)
        else:
            num_1 = int(value)
            option = "*"
            value = ""
            await message.answer(f'{num_1} {option} ', reply_markup=markup)
    elif message.text == '/':
        if value == "":
            await message.answer('Ошибка', reply_markup=markup)
        else:
            num_1 = int(value)
            option = "/"
            value = ""
            await message.answer(f'{num_1} {option} ', reply_markup=markup)
    elif message.text == 'c':
        if len(value) <= 1:
            value = ""
            await message.answer("0", reply_markup=markup)
        else:
            value = value[0:-1]
            await message.answer(value, reply_markup=markup)
    elif message.text == '=':
        if value == "":
            await message.answer('Ошибка!', reply_markup=markup)
        else:
            if option == "+":
                result = num_1 + int(value)
            elif option == "-":
                result = num_1 - int(value)
            elif option == "*":
                result = num_1 * int(value)
            elif option == "/":
                result = num_1 / int(value)
            else:
                result = -1
            temp = f"{num_1} {option} {int(value)} = {result}"
            await message.answer(f'{num_1} {option} {int(value)} = {result}', reply_markup=markup)
            value = ""
            num_1 = 0
            result = 0

            temp = str(message.date) + " " + str(message.from_user.first_name) + " " + str(
                message.from_user.last_name) + ": " + temp
            print(temp)

            # надо настроить
            # with open(filePath, 'a', encoding='UTF-8') as file:
            #     print(temp, file=file)
    else:
        await message.answer("Ошибка ввода!", reply_markup=markup)
        value = ""
        num_1 = 0
        result = 0
        option = ""


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    # executor.start_polling(dp)
    asyncio.run(main())
