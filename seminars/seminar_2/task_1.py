"""1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    *Пример:*
    - Для N = 5: 1, -3, 9, -27, 81
"""

# from random import *
# rnd = Random()
# n_list = []
# n = int(input("Введите число N: "))
# for i in range(n):
#     n_list.append(rnd.randint(-99, 99))
# print(n_list)

n_list = [1]
n = int(input("Введите число N: "))
for i in range(n - 1):
    n_list.append(n_list[i] * (-3))
print(n_list)
