# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

num_list = [2, 3, 4, 5, 6, 7, 8]
finish_list = []
for i in range(int(len(num_list) / 2) + 1):
    finish_list.append(num_list[i] * num_list[-i - 1])
print(finish_list)
