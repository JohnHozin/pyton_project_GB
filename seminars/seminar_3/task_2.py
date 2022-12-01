# Задайте список. Напишите программу,
# которая определит, присутствует ли в заданном списке строк некое число.

color_list = ['blue', 'green', 'white', 'gr2y', 'red']
num = 3
chek = False
# for i in color_list:
#     for j in i:
#         if j == str(num):
#             chek = True
#             break
# print(chek)

# for i in color_list:
#     if str(num) in i:
#         chek = True
#         break
# print(chek)

for i in color_list:
    if i.count(str(num)):
        chek = True
        break
print(chek)
