"""Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр"""

n = input("Введите число: ")
n_list = []
sum_num = 0
for i in range(len(n)):
    if n[i] == '.':
        continue
    sum_num += int(n[i])
print(sum_num)
