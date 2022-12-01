"""Напишите программу, которая принимает на вход вещественное число
 и показывает сумму его цифр"""


def check_is_number(n):
    if n.isdigit():
        return True
    else:
        num = n.split('.')
        if len(num) == 2:
            for i in num:
                if not i.isdigit():
                    return False
                return True
        else:
            return False


n = input("Введите число: ")
n_list = []
sum_num = 0
if check_is_number(n):
    for i in range(len(n)):
        if n[i] == '.':
            continue
        sum_num += int(n[i])
if sum_num == 0:
    print('Ошибка!')
else:
    print(sum_num)
