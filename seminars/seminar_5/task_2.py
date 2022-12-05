# В файле находится N натуральных чисел, записанных через пробел.
#   Среди чисел не хватает одного, чтобы выполнялось условие
#  A[i] - 1 = A[i-1]. Найдите это число.

with open('file.txt', 'r') as file:
    numbers = list(map(int, file.read().split()))
print(numbers)

for i in range(1, len(numbers)):
    if (numbers[i] - numbers[i - 1]) > 1:
        print(numbers[i] - 1)
        numbers.insert(i, numbers[i - 1] + 1)

print(numbers)

with open('file.txt', 'w') as file:
    # print(*numbers, file=file, sep=' ')
    file.write(' '.join(list(map(str, numbers))))
