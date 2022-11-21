""" Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них"""

numbers = [1, 4, 5, 6, 8]
max_num = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]
print(max_num)
