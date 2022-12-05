# Вычислить число Пи c заданной точностью d
# при d = 0.0001,  π = 3.1415
import math

print("Задача вычислить число Пи c заданной точностью d")
d = str(input("Введите число d: "))
print(math.pi)
d_len = len(d.split('.')[1])

# (максимум 15 знаков после запятой)
i = 0
num_pi = str(math.pi)
while i < (d_len + 2) and i < len(num_pi):
    print(num_pi[i], end="")
    i += 1

# 2 вариант (после 15 знаков после запятой выдаёт неверные значения) и округляет
# print()
# print(f'{math.pi:.{d_len}f}')

# def find_pi(n): # Ряд Мадхавы для вычисления пи всё равно не даёт много цифр после запятой
#     pi = 0
#     for i in range(n):
#         pi = pi + math.sqrt(12) * ((-1) ** i) / ((2 * i + 1) * (3 ** i))
#     print(pi)
#
#
# find_pi(600)
