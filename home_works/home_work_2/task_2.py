"""Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N"""

n = int(input("Введите число N: "))
n_list = []
for i in range(1, n + 1):
    if i == 1:
        n_list.append(i)
    else:
        temp = n_list[i - 2] * i
        n_list.append(temp)
print(n_list)
