# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# - Ввод:[1,1,2,4,5,6,7,7,8], результат: [2,4,5,6,8]

find_list = [1, 1, 2, 4, 5, 6, 7, 7, 8]
finish_list = []
for i in range(len(find_list)):
    repeat = False
    for j in range(len(find_list)):
        if find_list[i] == find_list[j] and i != j:
            repeat = True
            break
    if not repeat:
        finish_list.append(find_list[i])
print(f'{find_list} - исходный список')
print(f'{finish_list} - список без повторяющихся элементов')
