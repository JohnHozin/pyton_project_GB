# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

# List Comprehension
print(sum([i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0]))

# Filter
print(sum(filter(lambda i: i % 3 == 0 or i % 5 == 0, range(1, 1000))))

# Map
print(sum(map(lambda i: i if i % 3 == 0 or i % 5 == 0 else 0, range(1, 1000))))
