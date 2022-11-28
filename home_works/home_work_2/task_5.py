"""Реализуйте алгоритм перемешивания списка"""

from random import *

rnd = Random()
num_list = []
for i in range(40):
    num_list.append(rnd.randint(1, 50))
print(num_list)

max_num = num_list[0]
for i in range(len(num_list)):
    for j in range(len(num_list) - i - 1):
        if num_list[j + 1] < num_list[j]:
            temp = num_list[j + 1]
            num_list[j + 1] = num_list[j]
            num_list[j] = temp
print(num_list)


# time