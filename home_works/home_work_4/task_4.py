# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

n = int(input("Введите целое число: "))
num_list = []
for i in range(n + 1):
    num_list.append(str(random.randint(0, 100)))
print(num_list)
second_list = []
for i in range(len(num_list) - 1):
    if num_list[i] != "0":
        if num_list[i] == "1" and i == (len(num_list) - 2):
            second_list.append("x")
        elif num_list[i] == "1":
            second_list.append("x^" + str(len(num_list) - i - 1))
        elif i == (len(num_list) - 2):
            second_list.append(num_list[i] + "*x")
        else:
            second_list.append(num_list[i] + "*x^" + str(len(num_list) - i - 1))
if num_list[len(num_list) - 1] != 0:
    second_list.append(num_list[len(num_list) - 1])
print(*second_list, sep=' + ', end=' = 0')

with open('file.txt', 'a') as file:
    print(*second_list, file=file, sep=' + ', end=' = 0\n')
