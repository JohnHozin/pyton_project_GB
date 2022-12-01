"""Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число"""

import random

rnd = random.Random()
n_list = []
n = int(input("Введите число N: "))
for i in range(n):
    n_list.append(rnd.randint(-n, n))
print(n_list)

umn = 1
with open('file.txt', 'r') as data:
    for line in data:
        # print(line.strip())
        umn *= n_list[int(line.strip())]
print(umn)
