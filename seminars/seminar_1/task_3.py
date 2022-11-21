"""Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N"""

a = int(input("Введите число: "))
# nums = []
# for i in range(-abs(a), abs(a) + 1):  # abs это модуль числа
#     nums.append(i)
# print(nums)

for i in range(-abs(a), abs(a) + 1):
    print(i, end=' ')
