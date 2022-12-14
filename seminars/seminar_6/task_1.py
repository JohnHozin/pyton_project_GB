# Напишите программу вычисления арифметического
# выражения заданного строкой.Используйте операции +, -, /, *.приоритет
# операций стандартный. *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

line = input("Введите выражение: ")
line = line.split()
print(line)
result = 0

# def op(ch, line1):
#     for i in range(1, len(line1) - 1):
#         if line1[i] == ch:
#             if ch == "*":
#                 line1[i - 1] = int(line1[i - 1]) * int(line1[i + 1])
#             elif ch == "/":
#                 line1[i - 1] = int(line1[i - 1]) / int(line1[i + 1])
#             elif ch == "+":
#                 line1[i - 1] = int(line1[i - 1]) + int(line1[i + 1])
#             elif ch == "-":
#                 line1[i - 1] = int(line1[i - 1]) - int(line1[i + 1])
#             line1.pop(i + 1)
#             line1.pop(i)
#             break
#     return line1
#
#
# while len(line) > 1:
#     if line.count("*"):
#         line = op("*", line)
#     elif line.count("/"):
#         line = op("/", line)
#     elif line.count("+"):
#         line = op("+", line)
#     elif line.count("-"):
#         line = op("-", line)
#
# print(line[0])

#
# def op(ch, line1):
#     for i in range(1, len(line1) - 1):
#         if line1[i] == ch:
#             if ch == "*":
#                 line1[i - 1] = int(line1[i - 1]) * int(line1[i + 1])
#             elif ch == "/":
#                 line1[i - 1] = int(line1[i - 1]) / int(line1[i + 1])
#             elif ch == "+":
#                 line1[i - 1] = int(line1[i - 1]) + int(line1[i + 1])
#             elif ch == "-":
#                 line1[i - 1] = int(line1[i - 1]) - int(line1[i + 1])
#             line1.pop(i + 1)
#             line1.pop(i)
#             break
#     return line1


while len(line) > 1:
    if line.count("*") or line.count("/"):
        for i in range(1, len(line) - 1):
            if line[i] == "*":
                line[i - 1] = int(line[i - 1]) * int(line[i + 1])
                line.pop(i + 1)
                line.pop(i)
                break
            elif line[i] == "/":
                line[i - 1] = int(line[i - 1]) / int(line[i + 1])
                line.pop(i + 1)
                line.pop(i)
                break
    if line.count("+") or line.count("-"):
        for i in range(1, len(line) - 1):
            if line[i] == "+":
                line[i - 1] = int(line[i - 1]) + int(line[i + 1])
                line.pop(i + 1)
                line.pop(i)
                break
            elif line[i] == "-":
                line[i - 1] = int(line[i - 1]) - int(line[i + 1])
                line.pop(i + 1)
                line.pop(i)
                break


print(line)

# Формат: Объясняет преподаватель
#
# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# В этом случае можно пропустить совсем тривиальные (т.е. задачу 1 или 2 тут точно решать не имеет смысла) - исходите из уровня группы и студента.


# num = '1 * 2 * 3 / 5'
# num = num.split()
# print(num)
# while len(num) > 1:
#     while '*' in num or '/' in num :
#         if num.count('*') > 0 and num.count('/') > 0:
#             if num.index('/') > num.index('*'):
#                 num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
#                 num.pop(num.index('*') + 1)
#                 num.pop(num.index('*'))
#             else:
#                 num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
#                 num.pop(num.index('/') + 1)
#                 num.pop(num.index('/'))
#         else:
#             if '*' in num:
#                 num[num.index('*') - 1] = int(num[num.index('*') - 1]) * int(num[num.index('*') + 1])
#                 num.pop(num.index('*') + 1)
#                 num.pop(num.index('*'))
#             else:
#                 num[num.index('/') - 1] = int(num[num.index('/') - 1]) / int(num[num.index('/') + 1])
#                 num.pop(num.index('/') + 1)
#                 num.pop(num.index('/'))
# print(num)
