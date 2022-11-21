# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится)

x = int(input('Введите координату х: '))
y = int(input('Введите координату у: '))


def print_xy(x, y, z):
    print(f'x = {x}; y = {y} -> {z}')


if x > 0 and y > 0:
    print_xy(x, y, 1)
elif x > 0 and y < 0:
    print_xy(x, y, 4)
elif x < 0 and y > 0:
    print_xy(x, y, 2)
else:
    print_xy(x, y, 3)
