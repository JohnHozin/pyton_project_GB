# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

input_number = int(input("Введите целое число: "))
if input_number == 0:
    print(input_number)
    exit()

number = []
if input_number < 0:
    num = "-"
    input_number *= -1
else:
    num = ""

while input_number >= 1:
    number.append(int(input_number % 2))
    input_number = input_number / 2

for i in range(len(number)):
    num += str(number[-i - 1])
print(num)
