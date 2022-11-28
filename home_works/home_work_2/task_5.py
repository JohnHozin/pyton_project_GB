# Реализуйте алгоритм нахождения(генерации)
# рандомного(случайного) числа.(Не используя библиотеки связанные с рандомом) time

import time


def random_method(): # алгоритм нахождения случайного числа в интервале (0, 1)
    t = time.time()
    return round((t % 1 * 10 ** 6) % 1, 3)


num_list = []
for i in range(200): # создаём список из 200 случайных элементов
    num_list.append(random_method())
    time.sleep(0.001)
print(num_list)

max_num = num_list[0] # сортируем список
for i in range(len(num_list)):
    for j in range(len(num_list) - i - 1):
        if num_list[j + 1] < num_list[j]:
            temp = num_list[j + 1]
            num_list[j + 1] = num_list[j]
            num_list[j] = temp
print(num_list)
