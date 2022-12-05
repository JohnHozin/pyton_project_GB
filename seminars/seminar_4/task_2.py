# Найдите корни квадратного уравнения Ax² + Bx + C = 0

import math

# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))
str1 = '- 4 * x^2 + 4 * x - 1 = 0'
nums = str1.split()
nums1 = []
for i in nums:
    if i == '=':
        break
    if i.isdigit() or i == '-':
        nums1.append(i)

i = 0
while nums1.count('-') != 0:
    if nums1[i] == '-':
        nums1[i] += nums1[i + 1]
        nums1.pop(i + 1)
        i = 0
    i += 1
print(nums1)

a = float(nums1[0])
b = float(nums1[1])
c = float(nums1[2])


def find_diskriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    if d == 0:
        x = round(-b / (2 * a), 2)
        print(f'x= {x}')
    elif d > 0:
        x1 = round((-b + math.sqrt(d)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(d)) / (2 * a), 2)
        print(f'x1= {x1}')
        print(f'x2= {x2}')
    else:
        print('Корней нет')


find_diskriminant(a, b, c)
