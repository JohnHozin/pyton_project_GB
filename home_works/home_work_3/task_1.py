# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

num_list = [2, 3, 5, 9, 3]
print(num_list)
summa = 0
for i in range(len(num_list)):
    if i % 2 != 0:
        summa += num_list[i]
print(summa)
