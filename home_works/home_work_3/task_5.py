# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.

input_number = int(input("Введите целое число: "))


def fib(n): # функция Фибоначи
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def reverse_fib(n): # функция Негафибоначи
    return (-1) ** (n + 1) * fib(n)


fib_list = []
for i in range(input_number + 1):
    fib_list.append(reverse_fib(i))

fib_list.reverse()
fib_list.pop(-1)

for i in range(input_number + 1):
    fib_list.append(fib(i))
print(fib_list)
