# Напишите программу вычисления арифметического
# выражения заданного строкой.Используйте операции +, -, /, *.приоритет
# операций стандартный. *Пример: *
# 2 + 2 = > 4;
# 1 + 2 * 3 = > 7;
# 1 - 2 * 3 = > -5;

line = input("Введите выражение: ")
line = line.split()
# print(line)
result = 0

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

print(line[0])
