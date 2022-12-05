# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.(одинаковый размер уравнений)*
str_num_1 = ""
str_num_2 = ""

with open('file_for_5_1.txt', 'r') as file:
    for line in file:
        str_num_1 = line

with open('file_for_5_2.txt', 'r') as file:
    for line in file:
        str_num_2 = line

dict_1 = {}
dict_2 = {}
str_num_1 = str_num_1.split(" = ")[0]
str_num_2 = str_num_2.split(" = ")[0]
str_num_1_list = str_num_1.split(" + ")
str_num_2_list = str_num_2.split(" + ")
# print(str_num_1_list)
# print(str_num_2_list)
for i in range(len(str_num_1_list)):
    if str_num_1_list[i].count("x^"):
        dict_1[int(str_num_1_list[i].split("^")[1])] = int(str_num_1_list[i].split("*")[0])
    elif str_num_1_list[i].count("x"):
        dict_1[1] = int(str_num_1_list[i].split("*")[0])
    else:
        dict_1[0] = int(str_num_1_list[i])
print(dict_1)

for i in range(len(str_num_2_list)):
    if str_num_2_list[i].count("x^"):
        dict_2[int(str_num_2_list[i].split("^")[1])] = int(str_num_2_list[i].split("*")[0])
    elif str_num_2_list[i].count("x"):
        dict_2[1] = int(str_num_2_list[i].split("*")[0])
    else:
        dict_2[0] = int(str_num_2_list[i])
print(dict_2)

max_index = 0
for key in dict_1.keys():
    if max_index < key:
        max_index = key
for key in dict_2.keys():
    if max_index < key:
        max_index = key
# print(max_index)

dict_3 = {}
for i in range(max_index, -1, - 1):
    if i in dict_1:
        if i in dict_2:
            dict_3[i] = dict_1[i] + dict_2[i]
        else:
            dict_3[i] = dict_1[i]
    elif i in dict_2:
        dict_3[i] = dict_2[i]
print(dict_3)

final_list = []
for i in range(max_index, -1, - 1):
    # print(i, end=" ")
    if i in dict_3:
        # print(dict_3[i])
        if i == 1:
            final_list.append(str(dict_3[i]) + "*x")
        elif i == 0:
            final_list.append(str(dict_3[i]))
        else:
            final_list.append(str(dict_3[i]) + "*x^" + str(i))

with open('file_for_5.txt', 'a') as file:
    print(*final_list, file=file, sep=' + ', end=' = 0\n')
